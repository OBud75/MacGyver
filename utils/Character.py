import Maze

class MacGyver(object):
    def __init__(self, labyrinth):
        """Create the main character
        Args:
            labyrinth (object): Labyrinth in which MacGyver is trapped
        """
        self.labyrinth = labyrinth
        self.x = labyrinth.start[0].x
        self.y = labyrinth.start[0].y
        self.items_found = []

    def interaction(self):
        """User can quit typing 'quit'
            Asking for direction and calling check_block function
            If check_block is True then update x and y
        """
        print ("At any time, enter 'quit' to quit\n")
        while not self.labyrinth.game_over:
            print (f"You are row {self.x+1}, column {self.y+1}")
            print ("Items found:")
            for item in self.labyrinth.macgyver.items_found:
                print (f"{item['Name']}")
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
                    continue
                else:
                    break
            if Maze.Labyrinth.check_block(self.labyrinth, new_x, new_y):
                self.x, self.y = new_x, new_y
    
    def finding_item(self, item):
        print (f"You've found item: {item['Name']}")
        self.items_found.append(item)
        if len(self.items_found) == 3:
            print ("Compiling items...\nSyringe created!!")