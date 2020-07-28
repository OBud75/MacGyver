"""Here we create the main character of our labyrinth
The first attribute is the labyrinth he's in
MacGyver has a position (x, y) corresponding to the row and column that he's in
This position is initialized at the starting point
Another attribute is the list of items he found
The player moves MacGyver using the keyboard arrows (keydown) handled by pygame
This gives MacGyver a provisionary position (new_x, new_y)
The interaction uses the "check_block" method to return the type of block in the provisionary position
We update MacGyver's x and y if the provisionary position is a passage, the starting point, or contains an item
If the new block contains an item, we update MacGyver's "items_found" list
If all items are found, we update MacGyver's "items_found" list to the syringe
"""

# Third party imports
import pygame

# Local application imports
from utils import maze
from utils import graphics

class MacGyver:
    def __init__(self, labyrinth):
        """Create the main character
        Args:
            labyrinth (object): Labyrinth MacGyver is trapped in
        """
        self.labyrinth = labyrinth
        self.x = self.labyrinth.start[0].x
        self.y = self.labyrinth.start[0].y
        self.items_found = []

    def interaction(self):
        """Trying to move, provisionary block is new_x and new_y
        Call check_block to know if provisionary block is available
        Then update self.x and self.y depending on the result
        """
        # Getting new_x and new_y in dipend of user's input
        if self.event.key == pygame.K_UP:
            new_x, new_y = self.macgyver.x-1, self.macgyver.y
        elif self.event.key == pygame.K_DOWN:
            new_x, new_y = self.macgyver.x+1, self.macgyver.y
        elif self.event.key == pygame.K_LEFT:
            new_x, new_y = self.macgyver.x, self.macgyver.y-1
        elif self.event.key == pygame.K_RIGHT:
            new_x, new_y = self.macgyver.x, self.macgyver.y+1
        else:
            new_x, new_y = self.macgyver.x, self.macgyver.y

        # Calling check_block
        if maze.Labyrinth.check_block(self.labyrinth, new_x, new_y):
            self.macgyver.x, self.macgyver.y = new_x, new_y
    
    def finding_item(self, item):
        """Method called when check_block finds an item
        If user found all the items, he create a syringe

        Args:
            item (object): Item found
        """
        self.items_found.append(item['Name'])
        if len(self.items_found) == 3:
            self.items_found = "syringe"