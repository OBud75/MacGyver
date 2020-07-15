import pygame
from pygame.locals import *
import random

fichier_labyrinthe = "Labyrinthe.txt"

class Structure(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x};{self.y}"

class Labyrinthe(object):
    def __init__(self, fichier):
        width = 1
        height = 1
        for ligne in fichier:
            height +=1
            for case in ligne:
                width +=1
        self.width = width
        self.height = height

    def __repr__(self):
        return f"width = {self.width}, height = {self.height}"
    
    def niveau(self):
        liste_elmts = []
        liste_murs = []
        liste_passages = []
        liste_start = []
        liste_stop = []
        liste_items = []
        with open(fichier_labyrinthe, 'r') as lab:
            labyrinthe = lab.readlines()
            for line in labyrinthe:
                liste_elmts.append(line) 
        for x in range (self.width):
            for y in range (self.height):
                if liste_elmts[x][y] == "x":
                    mur = Structure(x, y)
                    liste_murs.append(mur)
                elif liste_elmts[x][y] == "o":
                    passage = Structure(x, y)
                    liste_passages.append(passage)
                elif liste_elmts[x][y] == "D":
                    depart = Structure(x, y)
                    liste_start.append(depart)
                else:
                    arrivee = Structure(x, y)
                    liste_stop.append(arrivee)
        position_items = random.choices(liste_passages, k=3)
        for position_passage in position_items:
            item = Structure(position_passage.x, position_passage.y)
            liste_items.append(item)
        self.murs = liste_murs
        self.passages = liste_passages
        self.start = liste_start
        self.stop = liste_stop
        self.items = liste_items
        return self.murs, self.passages, self.start, self.stop, self.items
        

class MacGyver(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"ligne {self.x +1}, colonne {self.y +1}"
    
    def checkcase(self, new_x, new_y):
        for mur in labyrinthe.murs:
            if mur.x == new_x and mur.y == new_y:
                print ("La case est prise par un mur")
                return False
        for item in labyrinthe.items:
            if item.x == new_x and item.y == new_y:
                print ("Vous avez trouvé un objet")
                labyrinthe.items.remove(item)
                return True
        for passage in labyrinthe.passages:
            if passage.x == new_x and passage.y == new_y:
                print ("Case libre")
                return True
        for depart in labyrinthe.start:
            if depart.x == new_x and depart.y == new_y:
                print ("Retour case départ")
                return True
        for arrivee in labyrinthe.stop:
            if arrivee.x == new_x and arrivee.y == new_y:
                if len(labyrinthe.items) == 0:
                    print ("Vous avez gagné")
                else:
                    print ("Vous n'avez pas trouvé tous les objets\nVous avez perdu")
                return "quitter"

    def interaction(self):
        mouvement = 0
        print ("A n'importe quel moment, entrez 'quitter' pour quitter")
        while mouvement != "quitter":
            print (f"Vous êtes {self}")
            mouvement = input ("Vers où voulez-vous aller?? (z = haut, s = bas, q = gauche, d = doite): ")
            if mouvement == "z":
                new_x = self.x-1
                new_y = self.y
                if self.checkcase(new_x, new_y) == True:
                    self.x = new_x
                    self.y = new_y
                elif self.checkcase(new_x, new_y) == "quitter":
                    mouvement = "quitter"
            elif mouvement == "s":
                new_x = self.x+1
                new_y = self.y
                if self.checkcase(new_x, new_y) == True:
                    self.x = new_x
                    self.y = new_y
                elif self.checkcase(new_x, new_y) == "quitter":
                    mouvement = "quitter"
            elif mouvement == "q":
                new_x = self.x
                new_y = self.y-1
                if self.checkcase(new_x, new_y) == True:
                    self.x = new_x
                    self.y = new_y
                elif self.checkcase(new_x, new_y) == "quitter":
                    mouvement = "quitter"
            elif mouvement == "d":
                new_x = self.x
                new_y = self.y+1
                if self.checkcase(new_x, new_y) == True:
                    self.x = new_x
                    self.y = new_y
                elif self.checkcase(new_x, new_y) == "quitter":
                    mouvement = "quitter"
            else:
                if mouvement != "quitter":
                    print ("Mouvement non reconnu")
    






labyrinthe = Labyrinthe(fichier_labyrinthe)
labyrinthe.niveau()
perso = MacGyver(labyrinthe.start[0].x, labyrinthe.start[0].y)

perso.interaction()

##########################################################
#                       Pygame                           #
##########################################################
"""
pygame.init()

fenetre = pygame.display.set_mode((640, 480))
pygame.display.set_caption("MacGyver")


pygame.display.flip()

continuer = 1
while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
"""