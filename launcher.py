#! /usr/bin/env python3

from utils import maze
from utils import character
from utils import graphics

def initializations():
    """Create instances of Labyrinth, MacGyver and Game

    Returns:
        Game instance: We'll launch the program with the method game_loop
    """
    labyrinth = maze.Labyrinth("labyrinth.txt")
    macgyver = character.MacGyver(labyrinth)
    game = graphics.Game(labyrinth, macgyver)
    return game

def main():
    game = initializations()
    graphics.Game.game_loop(game)
    

if __name__ == "__main__":
    main()