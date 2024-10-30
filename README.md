# Rock Paper Scissors Game

This is a simple Rock Paper Scissors game implemented in Python, featuring various player types that learn from their previous moves.

## Features:

- Multiple player types: Human, Random, Reflect, Cycle
- Players learn from previous moves
- Simple command-line interface

## Classes:

### Player
The base class for all players, defining the basic move and learn methods.

### HumanPlayer
Allows human input for moves via command line.

### RandomPlayer
Plays a random move each turn.

### ReflectPlayer
Plays the move that the opponent played last round.

### CyclePlayer
Cycles through the moves in the order of Rock -> Paper -> Scissors.

## Game Flow:
The game consists of three rounds. Each round, players make their moves, and the winner is determined based on the rules of Rock Paper Scissors.

## Installation:
Clone the repository and run the game using Python:

```bash
git clone https://github.com/Welat-E/rock_paper_scissors.git
cd rock_paper_scissors
python game.py
