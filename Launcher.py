#! /usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "utils"))
from utils import Maze, Character, Graphics

def initialization():
    labyrinth = Maze.Labyrinth("Labyrinth.txt")
    macgyver = Character.MacGyver(labyrinth)
    game = Graphics.Game(800, 800, labyrinth, macgyver)
    return game

def main():
    game = initialization()
    Graphics.Game.game_loop(game)
    

if __name__ == "__main__":
    main()