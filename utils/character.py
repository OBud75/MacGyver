"""Here we create the main character of our labyrinth
With the class "MacGyver"
We use agregation to create a more complex object
MacGyver takes "labyrinth" and "game" as attributes
"""

# Local application imports
from utils import graphics

class MacGyver:
    """The first attribute is the labyrinth he's in
    MacGyver has a position (x, y)
    That Correspond to the row and column that he's in
    This position is initialized at the starting point
    The last attribute is the list of items he found
    When MacGyver gets an item, we update MacGyver's "items_found" list
    If all items are found, we update MacGyver's "items_found" list to the syringe
    """
    def __init__(self, labyrinth):
        """Create the main character
        Args:
            labyrinth (object): Labyrinth MacGyver is trapped in
        """
        self.labyrinth = labyrinth
        self.game = graphics.Game(self.labyrinth, self)
        self.x_block = self.labyrinth.start[0]
        self.y_block = self.labyrinth.start[1]
        self.items_found = []

    def reset_position(self):
        """We will need this method if the user dies
        """
        self.x_block = self.labyrinth.start[0]
        self.y_block = self.labyrinth.start[1]

    def finding_item(self, item):
        """Method called when check_block finds an item
        If user found all the items, he create a syringe

        Args:
            item (object): Item found
        """
        self.game.show_text(f"You found: {item['Name']}!!", delay=1000)
        self.items_found.append(item['Name'])
        if len(self.items_found) == 3:
            self.game.show_text("You found all the items...",
                                x_block=3.5, y_block=5, delay=2000)
            self.game.show_text("You have created a syringe!!",
                                x_block=3, y_block=6, delay=1000)
            self.items_found = "syringe"

        # Refresh screen to erase messages
        graphics.Game.load_all(self)
