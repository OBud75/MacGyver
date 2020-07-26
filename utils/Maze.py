import random
import Structure
import Character

class Labyrinth(object):
    def __init__(self, file):
        """Create the structure of the labyrinth
        'o' for passages
        'x' for walls
        'D' for departure
        'A' for arrive
        Items will be create randomly in passages positions

        Args:
            file (.txt): File with the draw of the labyrinth
        """
        #File needed with the drawing of the labyrinth
        self.file = file
        width = 2
        height = 2
        for ligne in self.file:
            height +=1
            for case in ligne:
                width +=1
        self.width = width
        self.height = height
        #Creating the structure of the labyrinth
        list_elmts = []
        with open(self.file, 'r') as lab:
            for line in lab.readlines():
                list_elmts.append(line)
        #Check element and create appropriated structure
        self.walls = []
        self.passages = []
        self.start = []
        self.stop = []
        for x in range (self.height):
            for y in range (self.width):
                if list_elmts[x][y] == "x":
                    wall = Structure.Blocks(x, y)
                    self.walls.append(wall)
                elif list_elmts[x][y] == "o":
                    passage = Structure.Blocks(x, y)
                    self.passages.append(passage)
                elif list_elmts[x][y] == "D":
                    starting_point = Structure.Blocks(x, y)
                    self.start.append(starting_point)
                else:
                    arrive = Structure.Blocks(x, y)
                    self.stop.append(arrive)
        #Creating items in random positions in passages
        items_position = random.choices(self.passages, k=3)
        self.items = [
            {"Name": "Ether", "x": items_position[0].x, "y": items_position[0].y, "Image": "ether.png"},
            {"Name": "Needle", "x": items_position[1].x, "y": items_position[1].y, "Image": "aiguille.png"},
            {"Name": "Plastic tube",  "x": items_position[2].x, "y": items_position[2].y, "Image": "tube_plastique.png"}]
        #Character in the labyrinth
        self.macgyver = Character.MacGyver(self)
        #Stop the loop
        self.game_over = False
    
    def check_block(self, new_x, new_y):
        """Called when user is trying to move
        Args:
            new_x (int): Row the user is trying to go
            new_y (int): Column the user is trying to go
        Returns:
            Bool: Is the block free to go?
        """
        for wall in self.walls:
            if wall.x == new_x and wall.y == new_y:
                print ("There is a wall")
                return False
        for item in self.items:
            if item["x"] == new_x and item["y"] == new_y:
                Character.MacGyver.finding_item(self.macgyver, item)
                self.items.remove(item)
                return True
        for passage in self.passages:
            if passage.x == new_x and passage.y == new_y:
                print ("Free to go...")
                return True
        for starting_point in self.start:
            if starting_point.x == new_x and starting_point.y == new_y:
                print ("You're back at the starting point...")
                return True
        for end_point in self.stop:
            if end_point.x == new_x and end_point.y == new_y:
                self.arriving_point()

    def arriving_point(self):
        """Check if user got all the items
        If yes he won, else he lost
        """
        print ("Fighting guardian...")
        if len(self.items) == 0:
            print ("Using syringe...\nSeems to work!!\nYou won!!")
        else:
            print ("You lost...")
        self.game_over = True