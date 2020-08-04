#! /usr/bin/env python3

"""This file is used to launch the program
We first initialize all the instances of ths classes
The labyrinth is an instance of the class "Labyrinth"
It takes the .txt file where the labyrinth is draw as an argument
The main character is an instance of the class "MacGyver"
It takes the instance of the labyrinth we just created as an argument
Finally, the window of the game is an instance of the class "Game"
It takes both labyrinth and macgyver (instances we just created) as arguments
The program is launched with the "game_loop" method of the class "Game"
"""

# Local application imports
from utils import maze
from utils import character
from utils import graphics

def initializations():
    """Create instances of "Labyrinth", "MacGyver" and "Game"

    Returns:
        Game instance: Will be argument of the game loop method
    """
    labyrinth = maze.Labyrinth("labyrinth.txt")
    macgyver = character.MacGyver(labyrinth)
    game = graphics.Game(labyrinth, macgyver)
    return game

def main():
    """Call initializations and starts the game loop
    """
    game = initializations()
    graphics.Game.game_loop(game)
    

if __name__ == "__main__":
    main()