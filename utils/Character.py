import Maze
import pygame
import Graphics

class MacGyver(object):
    def __init__(self, labyrinth):
        """Create the main character
        Args:
            labyrinth (object): Labyrinth in which MacGyver is trapped
        """
        self.labyrinth = labyrinth
        self.x = self.labyrinth.start[0].x
        self.y = self.labyrinth.start[0].y
        self.items_found = []
        self.game = Graphics.Game(self.labyrinth, self)

    def interaction(self):
        """Trying to move, provisory block is new_x and new_y
        Call check_block to know if provisory block is available
        Then update self.x and self.y dipeding on the result
        """
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
        #Calling check_block
        if Maze.Labyrinth.check_block(self.labyrinth, new_x, new_y):
            self.macgyver.x, self.macgyver.y = new_x, new_y
    
    def finding_item(self, item):
        """Method called when check_block finds an item
        If user found all the items he create a syringe

        Args:
            item (object): Item found
        """
        self.items_found.append(item['Name'])
        if len(self.items_found) == 3:
            syringe = {"Name": "Syringe", "Image": "Images/seringue.png"}
            self.items_found = syringe["Name"]