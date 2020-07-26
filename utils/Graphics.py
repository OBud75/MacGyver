import os
import pygame
import Character

class Game(object):
    path_images = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Images")
    def __init__(self, width_pixels, height_pixels, labyrinth, macgyver):
        self.name = "MacGyver"
        self.icon = os.path.join(Game.path_images, "MacGyver.png")
        self.refreshtime = 100
        self.width_pixels = width_pixels
        self.height_pixels = height_pixels
        self.window = pygame.display.set_mode((self.width_pixels, self.height_pixels))
        self.labyrinth = labyrinth
        self.macgyver = macgyver
        pygame.display.set_caption(self.name)
        pygame.display.set_icon(pygame.image.load(self.icon))
        pygame.time.delay(self.refreshtime)

    def visual(self, image, x_block, y_block):
        self.x = round(x_block * self.height_pixels / self.labyrinth.height + self.height_pixels/200)
        self.y = round(y_block * self.width_pixels / self.labyrinth.width + self.width_pixels/200) 
        self.window.blit(pygame.image.load(image), (self.y, self.x))

    def game_loop(self):
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
            #Event handler
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.labyrinth.game_over = True
                elif self.event.type == pygame.KEYDOWN:
                    Character.MacGyver.interaction(self)
            #Update screen        
            pygame.display.update()