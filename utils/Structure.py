class Blocks:
    def __init__(self, x, y):
        """Create each blocks of the labyrinth:
        walls, passages, starting point and arriving point

        Args:
            x (int): Row
            y (int): Column
        """
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"{self.x+1};{self.y+1}"