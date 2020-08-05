"""Here we create the game window using the "pygame" package
The first 2 arguments are the labyrinth we want to display and Macgyver
Then we have the size of the window (height and width)
We need to decide how many pixels a block is going to take based on the size of the images
These images are stored in the "Images" directory in the main directory
To convert blocks into pixels, we will use the "block_to_pixels" method
We can change some window settings using "pygame" modules
In this case, we give the window a name and an icon
We create a "show_text" method that allow us to display text on the screen
We'll give this method the size, the position (x, y) of the text a delay and the color as arguments
By default, the text will be display at the center of the screen with no delay and in white
We now can start displaying the window with the "game_loop" method
Until "game_over" (see "maze" module) is False, the loop will continue
To display icons on the window we use the pygame's "blit" method
We first want to create visuals for each block and item
We do this using the "visual" method that takes the image and the position (x and y) as arguments
For our code to be more efficient, we create a method "load_all" that will load all the visuals
We call this method at the start of our "main_loop" and reload only MacGyver's icon at each loop
Others blocks will be reloaded only if needed
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

        # Paths to images and sounds
        self.path_images = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "Images")
        self.path_sounds = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "Sounds")

        # Window settings
        self.window = pygame.display.set_mode((self.width_pixels, self.height_pixels))
        pygame.display.set_caption("MacGyver")
        pygame.display.set_icon(pygame.image.load(
            os.path.join(self.path_images, "MacGyver.png")))

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
            R, G, B (int): Level of red, blue and green of the text (0 to 255)
        """
        font = pygame.font.Font("freesansbold.ttf", self.block_to_pixels(size))
        self.text = font.render(text, True, (R, G, B))
        self.window.blit(self.text, (self.block_to_pixels(x), self.block_to_pixels(y)))
        pygame.display.flip()
        pygame.time.delay(delay)

    def load_all(self):
        """This function will be called to load the visuals for each block
        Starting and arriving point, walls, passages, items and items found
        """
        # Starting point
        self.labyrinth.game.visual(
            os.path.join(self.labyrinth.game.path_images, "start_stop.png"),
            self.labyrinth.start.x, self.labyrinth.start.y)

        # Arriving point
        self.labyrinth.game.visual(
            os.path.join(self.labyrinth.game.path_images, "start_stop.png"),
            self.labyrinth.arrive.x, self.labyrinth.arrive.y)
        self.labyrinth.game.visual(
            os.path.join(self.labyrinth.game.path_images, "Gardien.png"),
            self.labyrinth.arrive.x, self.labyrinth.arrive.y)
        
        # Walls
        for wall in self.labyrinth.walls:
            self.labyrinth.game.visual(
                os.path.join(self.labyrinth.game.path_images, "wall.png"),
                wall.x, wall.y)

        # Passages
        for passage in self.labyrinth.passages:
            self.labyrinth.game.visual(
                os.path.join(self.labyrinth.game.path_images, "passage.png"),
                passage.x, passage.y)

        # Visuals of the items in the labyrinth
        for item in self.labyrinth.items:
            self.labyrinth.game.visual(os.path.join(
                self.labyrinth.game.path_images, item["Image"]),
                item["x"], item["y"])
        
        # Display a list of items found
        if self.labyrinth.macgyver.items_found:
            self.labyrinth.game.show_text(
                f"Bag: {self.labyrinth.macgyver.items_found}", x=2, y=0.2)

    def reload_block(self, old_x, old_y, block):
        """Method used when the user moves to reload the visual of his previous position
        If he found all the items, we use the visual of the syringe so it follows MacGyver
        In this case, we want to reload the passages too or the icon will be duplicated

        Args:
            old_x (int): Previous position (row)
            old_y (int): Previous position (column)
            block (str): Type of block we want to reload
        """
        if block == "start" :
            self.visual(os.path.join(self.path_images, "start_stop.png"), old_x, old_y)
        elif block == "passage" :
            self.visual(os.path.join(self.path_images, "passage.png"), old_x, old_y)
        elif block == "syringe" :
            for passage in self.labyrinth.passages :
                self.visual(os.path.join(self.path_images, "passage.png"), passage.x, passage.y)
            self.visual(os.path.join(self.path_images, "seringue.png"), old_x, old_y)

    def game_loop(self):
        """Main game loop
        Calling function to load all the visuals
        Then we get the events happening (quit or keydown)
        User tries to move using the keyboard arrows (keydown)
        This calls the method "interaction" of the "MacGyver" class
        """
        pygame.init()

        # Load all icons and music
        pygame.mixer.music.load(os.path.join(self.path_sounds, "music.wav"))
        pygame.mixer.music.play()
        self.load_all()

        # Loop until game over
        while self.labyrinth.game_over == False:

            # Visual of MacGyver
            self.visual(os.path.join(self.path_images, "MacGyver.png"),
                        self.macgyver.x, self.macgyver.y)

            # Event handler
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.labyrinth.game_over = True
                elif self.event.type == pygame.KEYDOWN:
                    character.MacGyver.interaction(self)

            # Update screen
            pygame.display.flip()
        pygame.quit()