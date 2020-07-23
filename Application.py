#! /usr/bin/env python3
import sys
import os
path = os.path.dirname(__file__)
path_utils = os.path.join(path, "utils")
sys.path.append(path_utils)
from utils import Maze
from utils import Character

def initialization():
    labyrinth = Maze.Labyrinth()
    macgyver = Character.MacGyver()
    return labyrinth, macgyver

def main():
    labyrinth, macgyver = initialization()
    print (labyrinth.items)
    macgyver.interaction()
    

if __name__ == "__main__":
    main()