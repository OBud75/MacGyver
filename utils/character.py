"""Here we create the main character of our labyrinth
To do this, we define the class "MacGyver"
We use agregation to create a more complex object
MacGyver takes "labyrinth" and "game" as attributes
"""

# Local application import
from utils import graphics

class MacGyver:
    """MacGyver has a position (x_block, y_block)
    That correspond to the row and column that he's in
    This position is initialized at the starting point
    The last attribute is the list of items he found
    When MacGyver gets an item, we update MacGyver's "items_found" list
    If all items are found, we update MacGyver's "items_found" list and create the syringe
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
        It resets MacGyver's position at the starting point
        """
        self.x_block = self.labyrinth.start[0]
        self.y_block = self.labyrinth.start[1]

    def finding_item(self, item):
        """Method called when check_block finds an item
        We add the item to the list of items found
        In addition, we display a message to inform the user
        If the user has found all the items, he creates a syringe

        Args:
            item (Dictionary): Item found
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
        self.game.load_all()
