"""Here we create the maze
To do this, we define the class "Labyrinth"
We use agregation to create a more complex object
Labyrinth takes "game" and "macgyver" as attributes
The "random" standard library is needed to create the items
"""

# Standard library import
import random

# Local application imports
from utils import character
from utils import graphics
from utils import constants

class Labyrinth:
    """We start defining the size by reading the .txt file we gave as an argument
    Continuing to read the file, we create a list of elements
    We can now create blocks for every kind of element in the list
    These elements are created with tuples containing their x and y coordinate
    That correspond to the row and the column they're in
    We have walls, passages, and a starting and arriving point
    Once this step is completed, the items can be created
    We need 3 items in random positions (they have to be in one of the passages)
    These items have a name, position (x and y), and an image associated with them
    We can know what's in each block using the "check_block" method
    This method takes the position (x and y) of the block we want to check
    If the block is the arriving point, it will call the "arriving_point" method
    If all items have been taken, the user won, else he dies and the game is reset
    If the user wins, this method will set "game_over" to True in order to exit the game
    """
    def __init__(self, file):
        """Create the structure of the labyrinth
        'o' for passages
        'x' for walls
        'D' for departure
        'A' for arrive

        Args:
            file (.txt): File with the draw of the labyrinth
        """
        # Define width, height and a list of all elements reading the file
        self.height = 0
        list_elmts = []
        with open(file, 'r') as lab:
            for line in lab.readlines():
                list_elmts.append(line)
                self.height += 1
                self.width = len(line)

        # Check every element and create appropriated structure
        self.walls = []
        self.passages = []
        for x_coordinate in range(self.height):
            for y_coordinate in range(self.width):
                if list_elmts[x_coordinate][y_coordinate] == "x":
                    wall = (x_coordinate, y_coordinate)
                    self.walls.append(wall)
                elif list_elmts[x_coordinate][y_coordinate] == "o":
                    passage = (x_coordinate, y_coordinate)
                    self.passages.append(passage)
                elif list_elmts[x_coordinate][y_coordinate] == "S":
                    self.start = (x_coordinate, y_coordinate)
                elif list_elmts[x_coordinate][y_coordinate] == "A":
                    self.arrive = (x_coordinate, y_coordinate)

        # Items creation
        items_position = random.choices(self.passages, k=3)
        self.items = [
            {"Name": "Ether", "Image": constants.ETHER_IMAGE,
             "x": items_position[0][0], "y": items_position[0][1]},

            {"Name": "Needle", "Image": constants.NEEDLE_IMAGE,
             "x": items_position[1][0], "y": items_position[1][1]},

            {"Name": "Plastic tube", "Image": constants.PLASTIC_TUBE_IMAGE,
             "x": items_position[2][0], "y": items_position[2][1]}]

        # Character and display of the labyrinth
        self.macgyver = character.MacGyver(self)
        self.game = graphics.Game(self, self.macgyver)

        # Will become True when arriving point is reached
        self.game_over = False
        self.restart = False

    def check_block(self, new_x, new_y):
        """Called when the user is trying to move
        Loop over each kind of structure to know what's in the new block

        Args:
            new_x (int): Row the user is trying to reach
            new_y (int): Column the user is trying to reach

        Returns:
            Boolean: Is the block free to go??
        """
        for wall in self.walls:
            if wall[0] == new_x and wall[1] == new_y:
                return False
        for item in self.items:
            if item["x"] == new_x and item["y"] == new_y:
                self.items.remove(item)
                character.MacGyver.finding_item(self.macgyver, item)
                return True
        for passage in self.passages:
            if passage[0] == new_x and passage[1] == new_y:
                return True
        if self.start[0] == new_x and self.start[1] == new_y:
            return True
        if self.arrive[0] == new_x and self.arrive[1] == new_y:
            self.arriving_point()
            return False

    def arriving_point(self):
        """Check if user got all the items
        If yes he won, or else he dies and the game restarts
        """
        if len(self.items) == 0:
            self.game.show_text("You won!!", x_block=3, size=2,
                                delay=3000, g_color=0, b_color=0)
            self.game_over = True
        else:
            self.game.show_text("You died...", x_block=3, size=2,
                                delay=3000, g_color=0, b_color=0)
            self.restart = True

        # Refresh screen to erase messages
        self.game.load_all()
