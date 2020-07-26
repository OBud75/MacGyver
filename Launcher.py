#! /usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "utils"))
from utils import Maze, Character, Graphics

def initializations():
    labyrinth = Maze.Labyrinth("Labyrinth.txt")
    macgyver = Character.MacGyver(labyrinth)
    game = Graphics.Game(labyrinth, macgyver)
    return game

def main():
    game = initializations()
    Graphics.Game.game_loop(game)
    

if __name__ == "__main__":
    main()