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
    
    def interaction(self):
        mouvement = 0
        print ("A n'importe quel moment, entrez 'quitter' pour quitter")
        while mouvement != "quitter":
            print (f"Vous êtes {self}")
            mouvement = input ("Vers où voulez-vous aller?? (z = haut, s = bas, q = gauche, d = doite): ")
            if mouvement == "z":
                for mur in labyrinthe.murs:
                    if mur.x == self.x-1 and mur.y == self.y:
                        print ("La case est prise par un mur")
                        break
                for item in labyrinthe.items:
                    if item.x == self.x-1 and item.y == self.y:
                        print ("Vous avez trouvé un objet")
                        labyrinthe.items.remove(item)
                for passage in labyrinthe.passages:
                    if passage.x == self.x-1 and passage.y == self.y:
                        self.x -= 1
                        break
                for depart in labyrinthe.start:
                    if depart.x == self.x-1 and depart.y == self.y:
                        print ("Retour case départ")
                        self.x -= 1
                        break
                for arrivee in labyrinthe.stop:
                    if arrivee.x == self.x-1 and arrivee.y == self.y:
                        if len(labyrinthe.items) == 0:
                            print ("Vous avez gagné")
                            mouvement = "quitter"
                        else:
                            print ("Vous n'avez pas trouvé tous les objets\nVous avez perdu")
                            mouvement = "quitter"
            elif mouvement == "s":
                for mur in labyrinthe.murs:
                    if mur.x == self.x+1 and mur.y == self.y:
                        print ("La case est prise par un mur")
                        break
                for item in labyrinthe.items:
                    if item.x == self.x+1 and item.y == self.y:
                        print ("Vous avez trouvé un objet")
                        labyrinthe.items.remove(item)
                for passage in labyrinthe.passages:
                    if passage.x == self.x+1 and passage.y == self.y:
                        self.x += 1
                        break
                for depart in labyrinthe.start:
                    if depart.x == self.x+1 and depart.y == self.y:
                        print ("Retour case départ")
                        self.x += 1
                        break
                for arrivee in labyrinthe.stop:
                    if arrivee.x == self.x+1 and arrivee.y == self.y:
                        if len(labyrinthe.items) == 0:
                            print ("Vous avez gagné")
                            mouvement = "quitter"
                        else:
                            print ("Vous n'avez pas trouvé tous les objets\nVous avez perdu")
                            mouvement = "quitter"
            elif mouvement == "q":
                for mur in labyrinthe.murs:
                    if mur.x == self.x and mur.y == self.y-1:
                        print ("La case est prise par un mur")
                        break
                for item in labyrinthe.items:
                    if item.x == self.x and item.y == self.y-1:
                        print ("Vous avez trouvé un objet")
                        labyrinthe.items.remove(item)
                for passage in labyrinthe.passages:
                    if passage.x == self.x and passage.y == self.y-1:
                        self.y -= 1
                        break
                for depart in labyrinthe.start:
                    if depart.x == self.x and depart.y == self.y-1:
                        print ("Retour case départ")
                        self.y -= 1
                        break
                for arrivee in labyrinthe.stop:
                    if arrivee.x == self.x and arrivee.y == self.y-1:
                        if len(labyrinthe.items) == 0:
                            print ("Vous avez gagné")
                            mouvement = "quitter"
                        else:
                            print ("Vous n'avez pas trouvé tous les objets\nVous avez perdu")
                            mouvement = "quitter"
            elif mouvement == "d":
                for mur in labyrinthe.murs:
                    if mur.x == self.x and mur.y == self.y+1:
                        print ("La case est prise par un mur")
                        break
                for item in labyrinthe.items:
                    if item.x == self.x and item.y == self.y+1:
                        print ("Vous avez trouvé un objet")
                        labyrinthe.items.remove(item)
                for passage in labyrinthe.passages:
                    if passage.x == self.x and passage.y == self.y+1:
                        self.y += 1
                        break
                for depart in labyrinthe.start:
                    if depart.x == self.x and depart.y == self.y+1:
                        print ("Retour case départ")
                        self.y += 1
                        break
                for arrivee in labyrinthe.stop:
                    if arrivee.x == self.x and arrivee.y == self.y+1:
                        if len(labyrinthe.items) == 0:
                            print ("Vous avez gagné")
                            mouvement = "quitter"
                        else:
                            print ("Vous n'avez pas trouvé tous les objets\nVous avez perdu")
                            mouvement = "quitter"
            else:
                if mouvement != "quitter":
                    print ("Mouvement non reconnu")
    

    def __repr__(self):
        return f"ligne {self.x +1}, colonne {self.y +1}"




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