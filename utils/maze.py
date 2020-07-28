"""Here we create the labyrinth object
We start defining the height and width by reading the .txt file we gave as argument
Continuing to read the file, we create a list of elements
We can now create instance attributes for every kind of element in the list
We have walls, passages, and a starting and arriving point
These objects are created with the "Blocks" class in the structure module
All of these objects have a position defined by their x and y
That correspond to the row and the column they're in
Once this step is completed, the items can be created
We need 3 items in random positions (they have to be in one of the passages)
These items have a name, position (x and y), and an image associated with them
We can know what's in each block using the "ckeck_block" method
This method takes the position (x and y) of the block we want to check
If the block is the arriving point, it will call the "arriving_point" method
If all items have been taken, the user won, else he lost
Then this method will set "game_over" to True in order to exit the game
"""

# Standard library imports
import random

# Local application imports
from utils import structure
from utils import character
from utils import graphics

class Labyrinth:
    def __init__(self, file):
        """Create the structure of the labyrinth
        Blocks are instances of the "Blocks" class in the "Structure" module
        'o' for passages
        'x' for walls
        'D' for departure
        'A' for arrive
        Items are created randomly in passage positions

        Args:
            file (.txt): File with the draw of the labyrinth
        """
        # Define width, height and a list of all elements reading the file
        self.file = file
        self.height = 0
        list_elmts = []
        with open(self.file, 'r') as lab:
            for line in lab.readlines():
                list_elmts.append(line)
                self.height += 1
                self.width = len(line)

        # Check every element and create appropriated structure
        self.walls = []
        self.passages = []
        self.start = []
        self.stop = []
        for x in range (self.height):
            for y in range (self.width):
                if list_elmts[x][y] == "x":
                    wall = structure.Blocks(x, y)
                    self.walls.append(wall)
                elif list_elmts[x][y] == "o":
                    passage = structure.Blocks(x, y)
                    self.passages.append(passage)
                elif list_elmts[x][y] == "D":
                    starting_point = structure.Blocks(x, y)
                    self.start.append(starting_point)
                elif list_elmts[x][y] == "A":
                    arrive = structure.Blocks(x, y)
                    self.stop.append(arrive)

        # Creating items in random positions in passages
        items_position = random.choices(self.passages, k=3)
        self.items = [
            {"Name": "Ether", "x": items_position[0].x, "y": items_position[0].y, "Image": "ether.png"},
            {"Name": "Needle", "x": items_position[1].x, "y": items_position[1].y, "Image": "aiguille.png"},
            {"Name": "Plastic tube",  "x": items_position[2].x, "y": items_position[2].y, "Image": "tube_plastique.png"}]

        # Character and display in the labyrinth
        self.macgyver = character.MacGyver(self)
        self.game = graphics.Game(self, self.macgyver)

        # Will become True when arriving point is reached
        self.game_over = False
    
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
            if wall.x == new_x and wall.y == new_y:
                return False
        for item in self.items:
            if item["x"] == new_x and item["y"] == new_y:
                character.MacGyver.finding_item(self.macgyver, item)
                self.items.remove(item)
                return True
        for passage in self.passages:
            if passage.x == new_x and passage.y == new_y:
                return True
        for starting_point in self.start:
            if starting_point.x == new_x and starting_point.y == new_y:
                return True
        for end_point in self.stop:
            if end_point.x == new_x and end_point.y == new_y:
                self.arriving_point()

    def arriving_point(self):
        """Check if user got all the items
        If yes he won, else he lost
        """
        if len(self.items) == 0:
            self.game.show_text("You won!!", size = 2, delay = 3000)
        else:
            self.game.show_text("You lost...", size = 2, delay = 3000)
        self.game_over = True