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
        return f"width = {self.width}, height = {self.height}"
    
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
        #For each raw of each column
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
        items = {}
        items_position = random.choices(list_passages, k=3)
        for i in range(len(items_position)):
            item = Structure(items_position[i].x, items_position[i].y)
            items[i] = item
        #Passing lists to class attributes
        self.walls = list_walls
        self.passages = list_passages
        self.start = list_start
        self.stop = list_stop
        self.items = items
        

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
        return f"Row {self.x +1}, column {self.y +1}"
    
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
            Calls end_game method if block is ending point
        """
        for wall in labyrinth.walls:
            if wall.x == new_x and wall.y == new_y:
                print ("There is a wall")
                return False
        for key in labyrinth.items.keys():
            if labyrinth.items[key].x == new_x and labyrinth.items[key].y == new_y:
                print ("You've found an item!!")
                del labyrinth.items[key]
                self.items_found.append(key)
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
        """Called by check_block when block is end point
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
        global run
        run = False

    def interaction(self):
        """User can quit typing 'quit'
            Asking for direction and calling check_block function
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
                if self.check_block(new_x, new_y):
                    self.move(new_x, new_y)
            elif self.movement == "s":
                new_x, new_y = self.x+1, self.y
                if self.check_block(new_x, new_y):
                    self.move(new_x, new_y)
            elif self.movement == "q":
                new_x, new_y = self.x, self.y-1
                if self.check_block(new_x, new_y):
                    self.move(new_x, new_y)
            elif self.movement == "d":
                new_x, new_y = self.x, self.y+1
                if self.check_block(new_x, new_y):
                    self.move(new_x, new_y)
            else:
                if self.movement != "quit":
                    print ("Movement not recognized")

    def moving_in_screen(self):
        print (macgyver.items_found)
        if event.key == pygame.K_UP:
            new_x, new_y = self.x-1, self.y
            if self.check_block(new_x, new_y):
                self.move(new_x, new_y)
        elif event.key == pygame.K_DOWN:
            new_x, new_y = self.x+1, self.y
            if self.check_block(new_x, new_y):
                self.move(new_x, new_y)
        elif event.key == pygame.K_LEFT:
            new_x, new_y = self.x, self.y-1
            if self.check_block(new_x, new_y):
                self.move(new_x, new_y)
        elif event.key == pygame.K_RIGHT:
            new_x, new_y = self.x, self.y+1
            if self.check_block(new_x, new_y):
                self.move(new_x, new_y)

#Initialization labyrinth and character
labyrinth = Labyrinth(file_labyrinth)
labyrinth.level()
macgyver = MacGyver(labyrinth.start[0].x, labyrinth.start[0].y)

##########################################################
#                       Pygame                           #
##########################################################

width = 800
height = 800

def launch (name, icone, refreshtime = 100, width = width, height = height):
    global window
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(name)
    pygame.display.set_icon(pygame.image.load(icone))
    pygame.display.flip()
    pygame.time.delay(refreshtime)

def visual(image, x, y, width = width, height = height):
    window.blit(pygame.image.load(image), (round(x*(width/(labyrinth.width+1))+5), round(y*(height/(labyrinth.height+1))+5)))


pygame.init()

launch("MacGyver", "Images/MacGyver.png")

run = True
while run == True:
    #Visuals for walls and passages
    for wall in labyrinth.walls:
        visual("Images/wall.png", wall.y, wall.x)
    for passage in labyrinth.passages:
        visual("Images/passage.png", passage.y, passage.x)
    #Visuals for items
    try:
        visual("Images/ether.png", labyrinth.items[0].y, labyrinth.items[0].x)
    except KeyError:
        pass
    try:
        visual("Images/aiguille.png", labyrinth.items[1].y, labyrinth.items[1].x)
    except KeyError:
        pass
    try:
        visual("Images/tube_plastique.png", labyrinth.items[2].y, labyrinth.items[2].x)
    except KeyError:
        pass
    #Visuals for start and end point, MacGyver and Guardian
    visual("Images/start_stop.png", labyrinth.start[0].y, labyrinth.start[0].x)
    visual("Images/start_stop.png", labyrinth.stop[0].y, labyrinth.stop[0].x)
    visual("Images/Gardien.png", labyrinth.stop[0].y, labyrinth.stop[0].x)
    visual("Images/MacGyver.png", macgyver.y, macgyver.x)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            macgyver.moving_in_screen()
    
    pygame.display.update()
    
pygame.quit()