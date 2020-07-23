import random
import Structure
import Character

class Labyrinth(object):
    def __init__(self):
        """Initialisation of the labytinth

        Args:
            file (.txt): File where the labyrinth is drawn
        """
        self.file = "Labyrinth.txt"
        width = 1
        height = 1
        for ligne in self.file:
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
        "x" for be walls
        "o" for be passages
        "D" for departure
        "A" for arrive

        Returns:
            Lists: Structure of the labyrinth
        """
        list_elmts = []
        list_walls = []
        list_passages = []
        list_start = []
        list_stop = []
        #Passing the .txt draw to a list of elements
        with open(self.file, 'r') as lab:
            for line in lab.readlines():
                list_elmts.append(line)
        #For each raw of each column
        for x in range (self.height+1):
            for y in range (self.width+1):
                #Check element and create appropriated structure
                if list_elmts[x][y] == "x":
                    wall = Structure.Blocks(x, y)
                    list_walls.append(wall)
                elif list_elmts[x][y] == "o":
                    passage = Structure.Blocks(x, y)
                    list_passages.append(passage)
                elif list_elmts[x][y] == "D":
                    starting_point = Structure.Blocks(x, y)
                    list_start.append(starting_point)
                else:
                    arrive = Structure.Blocks(x, y)
                    list_stop.append(arrive)
        #Creating items in random positions in passages
        items_position = random.choices(list_passages, k=3)
        items = {}
        items["Ether"] = Structure.Blocks(items_position[0].x, items_position[0].y)
        items["Needle"] = Structure.Blocks(items_position[1].x, items_position[1].y)
        items["Plastic tube"] = Structure.Blocks(items_position[2].x, items_position[2].y)
        #Passing lists to class attributes
        self.walls = list_walls
        self.passages = list_passages
        self.start = list_start
        self.stop = list_stop
        self.items = items
        return self.walls, self.passages, self.start, self.stop, self.items

    def check_block(self, new_x, new_y):
        """Called when user is trying to move
        Args:
            new_x (int): Row the user is trying to go
            new_y (int): Column the user is trying to go
        Returns:
            Bool: Is the block free to go?
            Calls end_game method if block is ending point
        """
        for wall in self.walls:
            if wall.x == new_x and wall.y == new_y:
                print ("There is a wall")
                return False
        for key in self.items.keys():
            if self.items[key].x == new_x and self.items[key].y == new_y:
                del self.items[key]
                Character.MacGyver.finding_item(self, key)
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
                Labyrinth.end_game(self)
    
    def end_game(self):
        """Called by check_block when block is end point
           list_items empty when reaching it??
           If yes then he won
           If not then he lost
           Quit the game
        """
        if len(self.items) == 0:
            print ("You won!!")
        else:
            print ("You did not find all the items...\nYou lost...")
        self.game_over = True