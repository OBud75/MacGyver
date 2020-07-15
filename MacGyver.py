import pygame
from pygame.locals import *
import random

fichier_labyrinth = "Labyrinth.txt"

class Structure(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x};{self.y}"

class Labyrinth(object):
    def __init__(self, fichier):
        width = 1
        height = 1
        for ligne in fichier:
            height +=1
            for case in ligne:
                width +=1
        self.width = width
        self.height = height

    def __repr__(self):
        return f"width = {self.width}, height = {self.height}"
    
    def level(self):
        list_elmts = []
        list_walls = []
        list_passages = []
        list_start = []
        list_stop = []
        list_items = []
        with open(fichier_labyrinth, 'r') as lab:
            labyrinth = lab.readlines()
            for line in labyrinth:
                list_elmts.append(line) 
        for x in range (self.height+1):
            for y in range (self.width+1):
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
        items_position = random.choices(list_passages, k=3)
        for passage_position in items_position:
            item = Structure(passage_position.x, passage_position.y)
            list_items.append(item)
        self.walls = list_walls
        self.passages = list_passages
        self.start = list_start
        self.stop = list_stop
        self.items = list_items
        return self.walls, self.passages, self.start, self.stop, self.items
        

class MacGyver(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"line {self.x +1}, column {self.y +1}"
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def checkcase(self, new_x, new_y):
        for wall in labyrinth.walls:
            if wall.x == new_x and wall.y == new_y:
                print ("There is a wall")
                return False
        for item in labyrinth.items:
            if item.x == new_x and item.y == new_y:
                print ("You've found an item")
                labyrinth.items.remove(item)
                return True
        for passage in labyrinth.passages:
            if passage.x == new_x and passage.y == new_y:
                print ("Free to go")
                return True
        for starting_point in labyrinth.start:
            if starting_point.x == new_x and starting_point.y == new_y:
                print ("You're at the starting point")
                return True
        for end_point in labyrinth.stop:
            if end_point.x == new_x and end_point.y == new_y:
                self.end_game()
    
    def end_game(self):
        if len(labyrinth.items) == 0:
            print ("You won")
        else:
            print ("You did not found all the items\nYou lost")
        self.movement = "quit"

    def interaction(self):
        self.movement = 0
        print ("At any time, enter 'quit' to quit")
        while self.movement != "quit":
            print (f"You are {self}")
            self.movement = input ("Which direction do you want to go?? (z = up, s = down, q = left, d = right): ")
            if self.movement == "z":
                new_x, new_y = self.x-1, self.y
                if self.checkcase(new_x, new_y) == True:
                    self.move(new_x, new_y)
            elif self.movement == "s":
                new_x, new_y = self.x+1, self.y
                if self.checkcase(new_x, new_y) == True:
                    self.move(new_x, new_y)
            elif self.movement == "q":
                new_x, new_y = self.x, self.y-1
                if self.checkcase(new_x, new_y) == True:
                    self.move(new_x, new_y)
            elif self.movement == "d":
                new_x, new_y = self.x, self.y+1
                if self.checkcase(new_x, new_y) == True:
                    self.move(new_x, new_y)
            else:
                if self.movement != "quit":
                    print ("Movement not recognized")
    






labyrinth = Labyrinth(fichier_labyrinth)
labyrinth.level()
char = MacGyver(labyrinth.start[0].x, labyrinth.start[0].y)
print (labyrinth.items)
print (labyrinth.width)
print (labyrinth.height)
print (labyrinth.walls)
char.interaction()

##########################################################
#                       Pygame                           #
##########################################################
"""
pygame.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("MacGyver")


pygame.display.flip()

continue = 1
while continue:
	for event in pygame.event.get():
		if event.type == QUIT:
			continue = 0
"""