import pygame
from pygame.locals import *
import random

file_labyrinth = "Labyrinth.txt"

class Structure(object):
    def __init__(self, x, y):
        """
            Create each blocks of the labyrinth:
            walls, passages, starting point,
            arriving point and items

        Args:
            x (int): Row
            y (int): Column
        """
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x+1};{self.y+1}"


class Labyrinth(object):
    def __init__(self, file):
        """Initialisation of the labytinth

        Args:
            file (.txt): File where the labyrinth is drawn
        """
        width = 1
        height = 1
        for ligne in file:
            height +=1
            for case in ligne:
                width +=1
        self.width = width
        self.height = height

    def __repr__(self):
        return f"width = {self.width+1}, height = {self.height+1}"
    
    def level(self):
        """Create elmts using Structure class
           Using the .txt file as follow
           "x" will be walls
           "o" will be passages
           "D" for departure
           "A" for arrive
        """
        list_elmts = []
        list_walls = []
        list_passages = []
        list_start = []
        list_stop = []
        #Passing the .txt draw to a list of elements
        with open(file_labyrinth, 'r') as lab:
            labyrinth = lab.readlines()
            for line in labyrinth:
                list_elmts.append(line)
        #For each raw(x) of each column(y)
        for x in range (self.height+1):
            for y in range (self.width+1):
                #Check element and create appropriated structure
                if list_elmts[x][y] == "x":
                    wall = Structure(x, y)
                    list_walls.append(wall)
                elif list_elmts[x][y] == "o":
                    passage = Structure(x, y)
                    list_passages.append(passage)
                elif list_elmts[x][y] == "D":
                    starting_point = Structure(x, y)
                    list_start.append(starting_point)
                else:
                    arrive = Structure(x, y)
                    list_stop.append(arrive)
        #Creating 3 items in random positions in passages
        list_items = []
        items_position = random.choices(list_passages, k=3)
        for passage_position in items_position:
            item = Structure(passage_position.x, passage_position.y)
            list_items.append(item)
        #Passing lists to class attributes
        self.walls = list_walls
        self.passages = list_passages
        self.start = list_start
        self.stop = list_stop
        self.items = list_items
        

class MacGyver(object):
    def __init__(self, x, y):
        """Create the main character

        Args:
            x (int): Position (row)
            y (int): Position (column)
        """
        self.x = x
        self.y = y
        self.items_found = []
    
    def __repr__(self):
        return f"line {self.x +1}, column {self.y +1}"
    
    def move(self, new_x, new_y):
        """Called to move if check_block returns True

        Args:
            new_x (int): New row
            new_y (int): New column
        """
        self.x = new_x
        self.y = new_y

    def check_block(self, new_x, new_y):
        """Called when user is trying to move

        Args:
            new_x (int): Row the user is trying to go
            new_y (int): Column the user is trying to go

        Returns:
            Bool: Is the block free to go?
        """
        for wall in labyrinth.walls:
            if wall.x == new_x and wall.y == new_y:
                print ("There is a wall")
                return False
        for item in labyrinth.items:
            if item.x == new_x and item.y == new_y:
                print ("You've found an item!!")
                labyrinth.items.remove(item)
                self.items_found.append(item)
                return True
        for passage in labyrinth.passages:
            if passage.x == new_x and passage.y == new_y:
                print ("Free to go...")
                return True
        for starting_point in labyrinth.start:
            if starting_point.x == new_x and starting_point.y == new_y:
                print ("You're back at the starting point...")
                return True
        for end_point in labyrinth.stop:
            if end_point.x == new_x and end_point.y == new_y:
                self.end_game()
    
    def end_game(self):
        """Called by check_block when case is end point
           list_items empty when reaching it??
           If yes then he won
           If not then he lost
           Quit the game
        """
        if len(labyrinth.items) == 0:
            print ("You won!!")
        else:
            print ("You did not find all the items...\nYou lost...")
        self.movement = "quit"

    def interaction(self):
        """User can quit typing 'quit'
           Asking for direction
           zsqd because french keyboard
           Calling check_block function
           If check_block is True then calls method move
        """
        self.movement = 0
        print ("At any time, enter 'quit' to quit\n")
        while self.movement != "quit":
            print (f"You are {self}")
            print (f"Items found: {self.items_found}")
            self.movement = input ("\nWhich direction do you want to go?? (z = up, s = down, q = left, d = right): ")
            if self.movement == "z":
                new_x, new_y = self.x-1, self.y
                if self.check_block(new_x, new_y) == True:
                    self.move(new_x, new_y)
            elif self.movement == "s":
                new_x, new_y = self.x+1, self.y
                if self.check_block(new_x, new_y) == True:
                    self.move(new_x, new_y)
            elif self.movement == "q":
                new_x, new_y = self.x, self.y-1
                if self.check_block(new_x, new_y) == True:
                    self.move(new_x, new_y)
            elif self.movement == "d":
                new_x, new_y = self.x, self.y+1
                if self.check_block(new_x, new_y) == True:
                    self.move(new_x, new_y)
            else:
                if self.movement != "quit":
                    print ("Movement not recognized")
    

labyrinth = Labyrinth(file_labyrinth)
labyrinth.level()
char = MacGyver(labyrinth.start[0].x, labyrinth.start[0].y)

print (f"Item position: {labyrinth.items}")

char.interaction()


##########################################################
#                       Pygame                           #
##########################################################

pygame.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("MacGyver")


pygame.display.flip()

display = 1
while display:
	for event in pygame.event.get():
		if event.type == QUIT:
			display = 0
