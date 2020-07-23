import Maze

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
        self.game_over = False

        self.file = "Labyrinth.txt"
        width = 1
        height = 1
        for ligne in self.file:
            height +=1
            for case in ligne:
                width +=1
        self.width = width
        self.height = height
        self.walls, self.passages, self.start, self.stop, self.items = Maze.Labyrinth.level(self)

    def __getattr__(self, name):
        return getattr(Maze.Labyrinth, name)

    def __repr__(self):
        return f"Row {self.x +1}, column {self.y +1}"
    
    def interaction(self):
        """User can quit typing 'quit'
            Asking for direction and calling check_block function
            If check_block is True then calls method move
        """
        print ("At any time, enter 'quit' to quit\n")
        while not self.game_over:
            print (f"You are {self}")
            print (f"Items found: {self.items_found}")
            self.movement = input ("\nWhich direction do you want to go?? (z = up, s = down, q = left, d = right): ")
            if self.movement == "z":
                new_x, new_y = self.x-1, self.y
            elif self.movement == "s":
                new_x, new_y = self.x+1, self.y
            elif self.movement == "q":
                new_x, new_y = self.x, self.y-1
            elif self.movement == "d":
                new_x, new_y = self.x, self.y+1
            else:
                if self.movement != "quit":
                    print ("Movement not recognized")
                    new_x, new_y = self.x, self.y
            if Maze.Labyrinth.check_block(self, new_x, new_y):
                self.move(new_x, new_y)

    def move(self, new_x, new_y):
        """Called to move if check_block returns True

        Args:
            new_x (int): New row
            new_y (int): New column
        """
        self.x = new_x
        self.y = new_y
    
    def finding_item(self, key):
        print (f"You've found item: {key}")
        self.items_found.append(key)