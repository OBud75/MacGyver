import os
import pygame
import Character

class Game(object):
    path_images = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Images")
    def __init__(self, labyrinth, macgyver):
        """Initialization of the game

        Args:
            labyrinth (object): Labyrinth in which MacGyver is trapped
            macgyver (object): Main character trapped in the labyrinth
        """
        #Width and height of the window
        self.width_pixels = 650
        self.height_pixels = 650
        #Window settings
        self.name = "MacGyver"
        self.icon = os.path.join(Game.path_images, "MacGyver.png")
        self.window = pygame.display.set_mode((self.width_pixels, self.height_pixels))
        self.refreshtime = 100
        self.labyrinth = labyrinth
        self.macgyver = macgyver
        pygame.display.set_caption(self.name)
        pygame.display.set_icon(pygame.image.load(self.icon))
        pygame.time.delay(self.refreshtime)

    def block_to_pixels(self, block):
        """Method used to convert blocks to pixels

        Args:
            block (int): size or position in blocks

        Returns:
            int: size or position in pixels
        """
        return round(block * self.height_pixels / self.labyrinth.height)

    def visual(self, image, x_block, y_block):
        """Method used to create visuals

        Args:
            image (.png): Path to image
            x_block (int): position x of the visual in blocks
            y_block (int): position y of the visual in blocks
        """
        x_pixels = self.block_to_pixels(x_block) 
        y_pixels = self.block_to_pixels(y_block)
        self.window.blit(pygame.image.load(image), (y_pixels, x_pixels))

    def show_text(self, text, x, y, taille):
        """Method used to show text on the screen

        Args:
            text (str): Text to print
            x (int): Position of the text (x) in blocks
            y (int): Position of the text (y) in blocks
            taille (int): Size of the text in blocks
        """
        font = pygame.font.Font("freesansbold.ttf", self.block_to_pixels(taille))
        self.text = font.render(text, True, (255, 255, 255))
        self.window.blit(self.text, (self.block_to_pixels(x), self.block_to_pixels(y)))

    def game_loop(self):
        """Main game loop
        """
        pygame.init()
        while self.labyrinth.game_over == False:
            #Structure of the labyrinth display
            for wall in self.labyrinth.walls:
                self.visual(os.path.join(Game.path_images, "wall.png"), wall.x, wall.y)
            for passage in self.labyrinth.passages:
                self.visual(os.path.join(Game.path_images, "passage.png"), passage.x, passage.y)
            for start in self.labyrinth.start:
                self.visual(os.path.join(Game.path_images, "start_stop.png"), start.x, start.y)
            for stop in self.labyrinth.stop:
                self.visual(os.path.join(Game.path_images, "start_stop.png"), stop.x, stop.y)
                self.visual(os.path.join(Game.path_images, "Gardien.png"), stop.x, stop.y)
            #Items display
            for item in self.labyrinth.items:
                self.visual(os.path.join(Game.path_images, item["Image"]), item["x"], item["y"])
            #MacGyver Display
            self.visual(os.path.join(Game.path_images, "MacGyver.png"), self.macgyver.x, self.macgyver.y)
            #Items display
            self.show_text(f"Items: {self.labyrinth.macgyver.items_found}", 1, 0, 0.75)
            #Event handler
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.labyrinth.game_over = True
                elif self.event.type == pygame.KEYDOWN:
                    Character.MacGyver.interaction(self)
            #Update screen
            pygame.display.flip()