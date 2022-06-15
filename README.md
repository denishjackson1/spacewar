# spacewar
Avatar Space War using Python

How in to run Space war program

Spacewar is an arcade game in the rich tradition of creating knockoffs of the original Spacewar! (considered one of the first computer games).

Background
Building something real is always a good way to force yourself to learn a program. It so happened that at the end of 2004 I wanted to learn python (for various reasons) and this game was the result. In 2016 I ported the game to the web using the Phaser game framework. Play it online.

Screenshots
The game menu:



1 human player against 3 AI players:



Game Play
Spacewar is a multi-player game. Each person controls a ship on a looping "toroid" plane. Each ship can rotate, has a thruster that accelerates the ship forward or backward, and has has a blaster weapon. There is also a sun in the center of the screen. All game objects exert gravitational force on all other objects. The sun is much more massive (but not larger) than other objects. Ships take damage if if they collide with a bullet, the sun, or another ship. Players score a point when they kill another player. If a player dies "accidentally", they lose a point.

The controls for each player are as follows:

Player 1:
    Left:     Left Arrow 
    Right:    Right Arrow 
    Thrust:   Up Arrow
    R-Thrust: Down Arrow
    Fire:     Right-Ctrl

Player 2:
    Left:     a
    Right:    d
    Thrust:   w
    R-Thrust: s
    Fire:     Tab

Player 3:
    Left:     j
    Right:    l
    Thrust:   i
    R-Thrust: k
    Fire:     Space

Player 4:
    Left:     Numpad 2
    Right:    Numpad 8
    Thrust:   Numpad 4
    R-Thrust: Numpad 5
    Fire:     Numpad 0
