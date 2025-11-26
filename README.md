# Alien-Ships

🛸 Alien Ships - Planetary Defense Game
Alien Ships is a text-based strategy game written in Python. You are the commander of Earth's defenses, tasked with locating and destroying invisible alien ships hiding in the asteroid belt surrounding our planet.

🎮 Game Overview
The game takes place on a 7x7 grid.

Earth (E) is located in the center of the sector (3, 3).

Asteroids (*) are scattered randomly around the board.

Alien Ships (X) are hidden. There are initially 2 ships.

Your goal is to guess the coordinates of the Alien Ships and fire upon them to destroy them. However, the aliens are smart—after every shot you take, the surviving ships will move to a new location!

✨ Features
Dynamic Board: A 7x7 grid utilizing texttable for clean console visualization.

Smart Enemy AI: Ships don't stay put. After every turn, they relocate either to the edge of the sector or attempt to close in on Earth.

Exception Handling: Custom error messages for invalid moves, hitting asteroids, or missing shots.

Cheat Mode: A developer tool to peek at the board and reveal ship locations.

Unit Testing: Includes a test suite to verify game logic.
