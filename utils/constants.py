"""Paths to images and sounds are constants
We define them in this file
The "os" standard library is needed to manipulate paths
"""

# Standard library import
import os

# Directories
PATH_IMAGES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Images")
PATH_SOUNDS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Sounds")

# Images files
MACGYVER_IMAGE = os.path.join(PATH_IMAGES, "MacGyver.png")
GUARDIAN_IMAGE = os.path.join(PATH_IMAGES, "Gardien.png")
START_STOP_IMAGE = os.path.join(PATH_IMAGES, "start_stop.png")
WALL_IMAGE = os.path.join(PATH_IMAGES, "wall.png")
PASSAGE_IMAGE = os.path.join(PATH_IMAGES, "passage.png")
ETHER_IMAGE = os.path.join(PATH_IMAGES, "ether.png")
NEEDLE_IMAGE = os.path.join(PATH_IMAGES, "aiguille.png")
PLASTIC_TUBE_IMAGE = os.path.join(PATH_IMAGES, "tube_plastique.png")
SYRINGE_IMAGE = os.path.join(PATH_IMAGES, "seringue.png")

# Music file
MUSIC = os.path.join(PATH_SOUNDS, "music.wav")
