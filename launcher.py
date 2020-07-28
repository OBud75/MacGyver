#! /usr/bin/env python3

"""In this file, we launch the program creating instances
The labyrinth is an instance of our class "Labyrinth" and takes the .txt file as an argument
The main character is an instance of the class "MacGyver" and takes the labyrinth as an argument
Finally, the game in itself is an instance of the class "Game"
It takes both labyrinth and macgyver as arguments
The program is launched by the game_loop method of the class "Game"
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