import pygame
import os
from pygame import time
pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = 700, 500  # defining width and heisght for the window frame.
IMAGE_WIDTH, IMAGE_HEIGHT = 50, 30
ROCKET = pygame.transform.scale(pygame.image.load(
    os.path.join('asset', 'rocket.png')), (IMAGE_WIDTH, IMAGE_HEIGHT))
SHIP = pygame.transform.scale(pygame.image.load(
    os.path.join('asset', 'fighter-jet.png')), (IMAGE_WIDTH, IMAGE_HEIGHT))

ROCKET_TRANSFORMED = pygame.transform.rotate(ROCKET, 90)
SHIP_TRANSFORMED = pygame.transform.rotate(SHIP, 0)

FPS = 60
VELOCITY = 5
BULLET_VEL = 9
MAX_BULLET = 10
ROCKET_HIT = pygame.USEREVENT + 1
SHIP_HIT = pygame.USEREVENT + 2
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 0, 255)
BLUE = (0, 255, 0)
BORDER = pygame.Rect(WIDTH/2-5, 0, 10, HEIGHT)
# adding the bullet soundtrack
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('asset', 'mixkit-8-bit-explosion-gun-2779.wav'))
ROCKET_HIT_SOUND = pygame.mixer.Sound(os.path.join('asset', 'mixkit-martial-arts-fast-punch-2047.wav'))
GAME_LEVEL_SOUND = pygame.mixer.Sound(os.path.join('asset', 'mixkit-game-level-music-689.wav'))

HEALTH_FONT = pygame.font.SysFont("comicsan", 40, bold=False, italic=False)
WINNER_FONT = pygame.font.SysFont("comicsan", 80, bold=False, italic=False)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
pygame.display.set_caption("SPACE WARS")


def draw_window(ship, rocket, ship_bullet, rocket_bullet, ship_health, rocket_health):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    ship_health_text = HEALTH_FONT.render(
        "A-Health: " + str(ship_health), 1, BLUE)
    rocket_health_text = HEALTH_FONT.render(
        "B-Health: " + str(rocket_health), 1, BLUE)
    WIN.blit(rocket_health_text, (WIDTH - ship_health_text.get_width()-10, 10))
    WIN.blit(ship_health_text, (10, 10))
    WIN.blit(SHIP_TRANSFORMED, (ship.x, ship.y))
    WIN.blit(ROCKET_TRANSFORMED, (rocket.x, rocket.y))
    for bullet in rocket_bullet:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in ship_bullet:
        pygame.draw.rect(WIN, GREEN, bullet)
    pygame.display.update()


def handle_rocket_movement(keys_pressed, rocket):
    if keys_pressed[pygame.K_a] and rocket.x - VELOCITY > BORDER.x:  # left
        rocket.x -= VELOCITY
    if keys_pressed[pygame.K_d] and rocket.x + VELOCITY + rocket.width < WIDTH:  # right
        rocket.x += VELOCITY
    if keys_pressed[pygame.K_w] and rocket.y + VELOCITY > 0:  # up
        rocket.y -= VELOCITY
    if keys_pressed[pygame.K_s] and rocket.y + VELOCITY + IMAGE_HEIGHT + 10 < HEIGHT:  # down
        rocket.y += VELOCITY


def handle_ship_movement(keys_pressed, ship):
    if keys_pressed[pygame.K_LEFT] and ship.x + VELOCITY > 0:  # left
        ship.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and ship.x + VELOCITY + IMAGE_WIDTH + 10 < BORDER.x:  # right
        ship.x += VELOCITY
    if keys_pressed[pygame.K_UP] and ship.y + VELOCITY > 0:  # up
        ship.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and ship.y + VELOCITY + IMAGE_HEIGHT + 10 < HEIGHT:  # down
        ship.y += VELOCITY


def handle_bullet(rocket_bullet, ship_bullet, rocket, ship):
    for bullet in rocket_bullet:
        bullet.x -= BULLET_VEL
        if ship.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SHIP_HIT))
            rocket_bullet.remove(bullet)
            ROCKET_HIT_SOUND.play()
        elif bullet.x < 0:
            rocket_bullet.remove(bullet)
    for bullet in ship_bullet:
        bullet.x += BULLET_VEL
        if rocket.colliderect(bullet):
            pygame.event.post(pygame.event.Event(ROCKET_HIT))
            ship_bullet.remove(bullet)
            ROCKET_HIT_SOUND.play()
        elif bullet.x > WIDTH:
            ship_bullet.remove(bullet)


def drwa_winner(text):
    winning_text = WINNER_FONT.render(text, 1, RED)
    WIN.blit(winning_text, (WIDTH//2 - winning_text.get_width() //
                            2, HEIGHT//2 - winning_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    rocket_bullet = []
    ship_bullet = []
    rocket = pygame.Rect(650, 100, IMAGE_WIDTH, IMAGE_HEIGHT)
    ship = pygame.Rect(50, 80, IMAGE_WIDTH, IMAGE_HEIGHT)
    run = True
    clock = pygame.time.Clock()
    rocket_health = 10
    ship_health = 10
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(rocket_bullet) < MAX_BULLET:
                    bullet = pygame.Rect(
                        rocket.x, rocket.y + rocket.height//2, 10, 5)
                    rocket_bullet.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(ship_bullet) < MAX_BULLET:
                    bullet = pygame.Rect(
                        ship.x + 5, ship.y + ship.height//2 - 2, 10, 5)
                    ship_bullet.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type == ROCKET_HIT:
                rocket_health -= 1

            if event.type == SHIP_HIT:
                ship_health -= 1
        winner = ""
        if rocket_health < 0:
            winner = "PLAYER A WON"
        if ship_health < 0:
            winner = "PLAYER B WON"
        if winner != "":
            drwa_winner(winner)
            GAME_LEVEL_SOUND.play()
            break

            # print(rocket_bullet, ship_bullet)
        keys_pressed = pygame.key.get_pressed()
        handle_rocket_movement(keys_pressed, rocket)
        handle_ship_movement(keys_pressed, ship)
        handle_bullet(rocket_bullet, ship_bullet, rocket, ship)

        draw_window(ship, rocket, ship_bullet, rocket_bullet,
                    ship_health, rocket_health)

    main()


if __name__ == "__main__":

    main()