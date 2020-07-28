import random
from utils import structure, character, graphics

class Labyrinth:
    def __init__(self, file):
        """Create the structure of the labyrinth
        Blocks are instances of the Blocks class in the Structure Module
        'o' for passages
        'x' for walls
        'D' for departure
        'A' for arrive
        Items are created randomly in passages positions

        Args:
            file (.txt): File with the draw of the labyrinth
        """
        self.file = file
        #Define width, height and a list of all elements reading the file
        self.height = 0
        list_elmts = []
        with open(self.file, 'r') as lab:
            for line in lab.readlines():
                list_elmts.append(line)
                self.height += 1
                self.width = len(line)
        #Check every element and create appropriated structure
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
                else:
                    arrive = structure.Blocks(x, y)
                    self.stop.append(arrive)
        #Creating items in random positions in passages
        items_position = random.choices(self.passages, k=3)
        self.items = [
            {"Name": "Ether", "x": items_position[0].x, "y": items_position[0].y, "Image": "ether.png"},
            {"Name": "Needle", "x": items_position[1].x, "y": items_position[1].y, "Image": "aiguille.png"},
            {"Name": "Plastic tube",  "x": items_position[2].x, "y": items_position[2].y, "Image": "tube_plastique.png"}]
        #Character and display in the labyrinth
        self.macgyver = character.MacGyver(self)
        self.game = graphics.Game(self, self.macgyver)
        #Will become True when arriving point is reached
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
            self.game.show_text("You won!!")
        else:
            self.game.show_text("You lost...")
        self.game_over = True
