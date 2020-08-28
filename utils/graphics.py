"""Here we create the game window
To do this, we define the class "Game"
We use agregation to create a more complex object
Game takes "macgyver" and "labyrinth" as attributes
The "pygame" third party library is used to manage all the graphics
The "PIL" third party library is used to settle the size of a block
"""

# Third party import
from PIL import Image
import pygame

# Local application import
from utils import constants
from utils import maze

class Game:
    """We first need to settle how many pixels a block is going to take
    We define this based on the size of the icons with the "PIL.Image" module
    These images are stored in the "Images" directory in the main directory
    To convert blocks into pixels, we will use the "block_to_pixels" method
    We can now define the size of the window
    We can change some window settings using "pygame" modules
    In this case, we give the window a name and an icon
    We create a "show_text" method that allow us to display text on the screen
    We first want to create visuals for each block and item
    We do this using the "visual" method
    Those 2 methods use the pygame's "blit" method
    For our code to be more efficient, we create a method "load_all" that will load all the visuals
    We call this method at the start of our "main_loop" and reload only MacGyver's icon at each loop
    Others blocks will be reloaded only if needed
    Pygame's "event.get()" method allows us to handle the user's inputs
    If the user presses a keyboard arrow, it will call the "interaction" method
    """
    def __init__(self, labyrinth, macgyver):
        """Initialize the game object with window properties
        Converting blocks logic into pixels with "block_to_pixels" method

        Args:
            labyrinth (instance of Labyrinth): Structure of the labyrinth
            macgyver (instance of MacGyver): Main character moving
        """
        self.labyrinth = labyrinth
        self.macgyver = macgyver

        # Width and height of the window
        self.block_size = Image.open(constants.WALL_IMAGE).size[0]
        width_pixels = self.block_to_pixels(self.labyrinth.width)
        height_pixels = self.block_to_pixels(self.labyrinth.height)

        # Window settings
        self.window = pygame.display.set_mode((width_pixels, height_pixels))
        pygame.display.set_caption("MacGyver")
        pygame.display.set_icon(pygame.image.load(constants.MACGYVER_IMAGE))

    def block_to_pixels(self, block):
        """Convert block logic into pixels

        Args:
            block (int): Value in blocks

        Returns:
            int: Value in pixels
        """
        return round(block * self.block_size)

    def visual(self, image, x_block, y_block):
        """Method used to create visuals

        Args:
            image (.png): Image we want to display
            x_block (int): Position of the visual in blocks (raw)
            y_block (int): Position of the visual in blocks (column)
        """
        x_pixels = self.block_to_pixels(x_block)
        y_pixels = self.block_to_pixels(y_block)
        self.window.blit(pygame.image.load(image), (y_pixels, x_pixels))

    def show_text(self, text, x_block=4, y_block=4, size=0.75,
                  delay=0, r_color=255, g_color=255, b_color=255):
        """Method used to show text on the screen

        Args:
            text (str): Text to print
            x_blobs (int): Position of the text (vertical align) in blocks
            y_block (int): Position of the text (horizontal align) in blocks
            size (int): Size of the text in blocks
            delay (int): Delay time while showing the text in miliseconds
            r_color (int): Level of red of the text (0 to 255)
            g_color (int): Level of green of the text (0 to 255)
            b_color (int): Level of blue of the text (0 to 255)
        """
        font = pygame.font.Font("freesansbold.ttf", self.block_to_pixels(size))
        text = font.render(text, True, (r_color, g_color, b_color))
        self.window.blit(text, (self.block_to_pixels(x_block), self.block_to_pixels(y_block)))
        pygame.display.flip()
        pygame.time.delay(delay)

    def load_all(self):
        """This function will be called to load the visuals for each block
        Starting and arriving point, walls, passages and items
        It will also display the list of MacGyver's items
        """
        # Starting point
        self.labyrinth.game.visual(constants.START_STOP_IMAGE,
                                   self.labyrinth.start[0], self.labyrinth.start[1])

        # Arriving point
        self.labyrinth.game.visual(constants.START_STOP_IMAGE,
                                   self.labyrinth.arrive[0], self.labyrinth.arrive[1])
        self.labyrinth.game.visual(constants.GUARDIAN_IMAGE,
                                   self.labyrinth.arrive[0], self.labyrinth.arrive[1])

        # Walls
        for wall in self.labyrinth.walls:
            self.labyrinth.game.visual(constants.WALL_IMAGE, wall[0], wall[1])

        # Passages
        for passage in self.labyrinth.passages:
            self.labyrinth.game.visual(constants.PASSAGE_IMAGE, passage[0], passage[1])

        # Visuals of the items in the labyrinth
        for item in self.labyrinth.items:
            self.labyrinth.game.visual(item["Image"], item["x"], item["y"])

        # Display a list of items found
        if self.labyrinth.macgyver.items_found:
            self.labyrinth.game.show_text(
                f"Bag: {self.labyrinth.macgyver.items_found}", x_block=2, y_block=0.2)

    def reload_block(self, old_x, old_y, block):
        """Method used when the user moves to reload the visual of his previous position
        If he found all the items, we use the visual of the syringe so it follows MacGyver
        In this case, we want to reload the passages too or the icon will be duplicated

        Args:
            old_x (int): Previous position (row)
            old_y (int): Previous position (column)
            block (str): Type of block we want to reload
        """
        if block == "start":
            self.visual(constants.START_STOP_IMAGE, old_x, old_y)
        elif block == "passage":
            self.visual(constants.PASSAGE_IMAGE, old_x, old_y)
        elif block == "syringe":
            for passage in self.labyrinth.passages:
                self.visual(constants.PASSAGE_IMAGE, passage[0], passage[1])
            self.visual(constants.SYRINGE_IMAGE, old_x, old_y)

    def interaction(self, event):
        """Trying to move, the provisionary block is new_x and new_y
        Call check_block to know if the provisionary block is available
        Then update self.x and self.y depending on the result
        Finally, we reload the visual of the previous position

        Args:
            event (pygame event): A key has been pressed
        """
        old_x, old_y = self.macgyver.x_block, self.macgyver.y_block

        # Gets new_x and new_y in dipend of user's input
        if event == pygame.K_UP:
            new_x, new_y = self.macgyver.x_block-1, self.macgyver.y_block
        elif event == pygame.K_DOWN:
            new_x, new_y = self.macgyver.x_block+1, self.macgyver.y_block
        elif event == pygame.K_LEFT:
            new_x, new_y = self.macgyver.x_block, self.macgyver.y_block-1
        elif event == pygame.K_RIGHT:
            new_x, new_y = self.macgyver.x_block, self.macgyver.y_block+1
        else:
            new_x, new_y = self.macgyver.x_block, self.macgyver.y_block

        # Calls check_block
        if maze.Labyrinth.check_block(self.labyrinth, new_x, new_y):
            self.macgyver.x_block, self.macgyver.y_block = new_x, new_y

        # Reloads visual of the old position
        if self.labyrinth.start[0] == old_x and self.labyrinth.start[1] == old_y:
            self.reload_block(old_x, old_y, block="start")
        elif self.labyrinth.macgyver.items_found == "syringe":
            self.reload_block(old_x, old_y, block="syringe")
        else:
            self.reload_block(old_x, old_y, block="passage")

    def game_loop(self):
        """Main game loop
        We first call functions to load the music, items and all the visuals
        Then we get the events happening (quit or keydown)
        User tries to move using the keyboard arrows (keydown)
        This calls the method "interaction"
        We reload MacGyver's icon at each loop
        If the user dies, we restart the game, resetting MacGyver's position and the items
        """
        pygame.init()

        # Load the music and the graphics
        pygame.mixer.music.load(constants.MUSIC)
        pygame.mixer.music.play(loops=-1)
        self.load_all()

        # Loop until game over
        while not self.labyrinth.game_over:

            # Visual of MacGyver
            self.visual(constants.MACGYVER_IMAGE, self.macgyver.x_block, self.macgyver.y_block)

            # Event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.labyrinth.game_over = True
                elif event.type == pygame.KEYDOWN:
                    self.interaction(event.key)

            # If player dies
            if self.labyrinth.restart:
                self.macgyver.reset_position()
                self.labyrinth.restart = False

            # Update screen
            pygame.display.flip()
        pygame.quit()
