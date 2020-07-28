"""We use this class to create the structure of the labyrinth
"""

class Blocks:
    def __init__(self, x, y):
        """Create each blocks of the labyrinth
        Walls, passages, starting point and arriving point

        Args:
            x (int): Row
            y (int): Column
        """
        self.x = x
        self.y = y
