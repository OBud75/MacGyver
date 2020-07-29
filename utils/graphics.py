"""Here we create the game window using the "pygame" package
The first 2 arguments are the labyrinth we want to display and Macgyver
Then we have the size of the window (height and width)
We need to decide how many pixels a block is going to take based on the size of the images
These images are stored in the "Images" directory in the main directory
To convert blocks into pixels, we will use the "block_to_pixels" method
We can change some window settings using "pygame" modules
In this case, we give the window a name and an icon
We now can start displaying the window with the "game_loop" method
Until "game_over" (see "maze" module) is False, the loop will continue
To display things on the window we use the pygame's "blit" method
We first want to create visuals for each block and item
We do this using the "visual" method that takes the image and the position (x and y) as arguments
Then we show text on the screen using the "show_text" method
We'll give this method the size, the position (x, y) of the text and a delay as arguments
By default, the text will be display at the center of the screen with no delay
Pygame's "event.get()" method allows us to handle the user's inputs
If the user presses a keyboard arrow, it will call the "interaction" method of the "character" module
"""

# Standard library imports
import os

# Third party imports
import pygame

# Local application imports
from utils import character

class Game:
    def __init__(self, labyrinth, macgyver):
        """Initialize the game object with window properties
        Converting blocks logic into pixels with "block_to_pixels" method

        Args:
            labyrinth (object): Structure of the labyrinth
            macgyver (object): Main character moving
        """
        self.labyrinth = labyrinth
        self.macgyver = macgyver

        # Width and height of the window
        self.block_size = 43
        self.width_pixels = self.block_to_pixels(self.labyrinth.width)
        self.height_pixels = self.block_to_pixels(self.labyrinth.height)

        # Window settings
        self.path_images = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Images")
        self.window = pygame.display.set_mode((self.width_pixels, self.height_pixels))
        pygame.display.set_caption("MacGyver")
        pygame.display.set_icon(pygame.image.load(os.path.join(self.path_images, "MacGyver.png")))

    def block_to_pixels(self, block):
        """Convert blocks to pixels

        Args:
            block (int): Value in blocks

        Returns:
            int: Value in pixels
        """
        return round(block * self.block_size)

    def visual(self, image, x_block, y_block):
        """Method used to create visuals

        Args:
            image (.png): Path to image
            x_block (int): Position of the visual in blocks (raw)
            y_block (int): Position of the visual in blocks (column)
        """
        x_pixels = self.block_to_pixels(x_block) 
        y_pixels = self.block_to_pixels(y_block)
        self.window.blit(pygame.image.load(image), (y_pixels, x_pixels))

    def show_text(self, text, x=4, y=4, size=0.75, delay=0, R=255, G=255, B=255):
        """Method used to show text on the screen

        Args:
            text (str): Text to print
            x (int): Position of the text (vertical align) in blocks
            y (int): Position of the text (horizontal align) in blocks
            size (int): Size of the text in blocks
            delay (int): Delay time while showing the text in miliseconds
        """
        font = pygame.font.Font("freesansbold.ttf", self.block_to_pixels(size))
        self.text = font.render(text, True, (R, G, B))
        self.window.blit(self.text, (self.block_to_pixels(x), self.block_to_pixels(y)))
        pygame.display.flip()
        pygame.time.delay(delay)

    def game_loop(self):
        """Main game loop
        Loading visuals for each block, character, items and items found
        Then we get the events happening (quit or keydown)
        User tries to move using the keyboard arrows (keydown)
        This calls the method "interaction" of the "MacGyver" class
        """
        pygame.init()
        while self.labyrinth.game_over == False:

            # Visuals of the structure of the labyrinth
            for wall in self.labyrinth.walls:
                self.visual(os.path.join(self.path_images, "wall.png"), wall.x, wall.y)
            for passage in self.labyrinth.passages:
                self.visual(os.path.join(self.path_images, "passage.png"), passage.x, passage.y)
            for start in self.labyrinth.start:
                self.visual(os.path.join(self.path_images, "start_stop.png"), start.x, start.y)
            for stop in self.labyrinth.stop:
                self.visual(os.path.join(self.path_images, "start_stop.png"), stop.x, stop.y)
                self.visual(os.path.join(self.path_images, "Gardien.png"), stop.x, stop.y)

            # Visuals of the items
            for item in self.labyrinth.items:
                self.visual(os.path.join(self.path_images, item["Image"]), item["x"], item["y"])
            if self.labyrinth.macgyver.items_found:
                self.show_text(f"Bag: {self.labyrinth.macgyver.items_found}", x=2, y=0.2)
            if self.labyrinth.macgyver.items_found == "syringe":
                self.visual(os.path.join(self.path_images, "seringue.png"), self.macgyver.x-1, self.macgyver.y)

            # Visual of MacGyver
            self.visual(os.path.join(self.path_images, "MacGyver.png"), self.macgyver.x, self.macgyver.y)

            # Event handler
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.labyrinth.game_over = True
                elif self.event.type == pygame.KEYDOWN:
                    character.MacGyver.interaction(self)

            # Update screen
            pygame.display.flip()
        pygame.quit()