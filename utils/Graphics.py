import os
import pygame
import Character

class Game:
    def __init__(self, labyrinth, macgyver):
        """Initialize the game object with window properties
        Converting blocks logic in pixels with block_to_pixels method

        Args:
            labyrinth (object): Structure of the labyrinth
            macgyver (object): Main character moving
        """
        self.labyrinth = labyrinth
        self.macgyver = macgyver
        #Images directory
        self.path_images = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Images")
        #Width and height of the window
        self.block_size = 43
        self.width_pixels = self.block_to_pixels(self.labyrinth.width)
        self.height_pixels = self.block_to_pixels(self.labyrinth.height)
        #Window settings
        self.window = pygame.display.set_mode((self.width_pixels, self.height_pixels))
        pygame.display.set_caption("MacGyver")
        pygame.display.set_icon(pygame.image.load(os.path.join(self.path_images, "MacGyver.png")))
        pygame.time.delay(100)

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
            x_block (int): position of the visual in blocks (raw)
            y_block (int): position of the visual in blocks (column)
        """
        x_pixels = self.block_to_pixels(x_block) 
        y_pixels = self.block_to_pixels(y_block)
        self.window.blit(pygame.image.load(image), (y_pixels, x_pixels))

    def show_text(self, text, x, y, size):
        """Method used to show text on the screen

        Args:
            text (str): Text to print
            x (int): Position of the text (vertical align) in blocks
            y (int): Position of the text (horizontal align) in blocks
            size (int): Size of the text in blocks
        """
        font = pygame.font.Font("freesansbold.ttf", self.block_to_pixels(size))
        self.text = font.render(text, True, (255, 255, 255))
        self.window.blit(self.text, (self.block_to_pixels(x), self.block_to_pixels(y)))

    def game_loop(self):
        """Main game loop
        Loading visuals for each block, character, items and items found
        User moves using the keyboard arrows
        It will call the method interaction in the MacGyver class
        """
        pygame.init()
        while self.labyrinth.game_over == False:
            #Structure of the labyrinth display
            for wall in self.labyrinth.walls:
                self.visual(os.path.join(self.path_images, "wall.png"), wall.x, wall.y)
            for passage in self.labyrinth.passages:
                self.visual(os.path.join(self.path_images, "passage.png"), passage.x, passage.y)
            for start in self.labyrinth.start:
                self.visual(os.path.join(self.path_images, "start_stop.png"), start.x, start.y)
            for stop in self.labyrinth.stop:
                self.visual(os.path.join(self.path_images, "start_stop.png"), stop.x, stop.y)
                self.visual(os.path.join(self.path_images, "Gardien.png"), stop.x, stop.y)
            #Items display
            for item in self.labyrinth.items:
                self.visual(os.path.join(self.path_images, item["Image"]), item["x"], item["y"])
            if self.labyrinth.macgyver.items_found:
                self.show_text(f"Items: {self.labyrinth.macgyver.items_found}", 2, 0, 0.75)
            #MacGyver Display
            self.visual(os.path.join(self.path_images, "MacGyver.png"), self.macgyver.x, self.macgyver.y)
            #Event handler
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.labyrinth.game_over = True
                elif self.event.type == pygame.KEYDOWN:
                    Character.MacGyver.interaction(self)
            #Update screen
            pygame.display.flip()
        pygame.quit()