class Cell:
    def __init__(self, row, col):
        self.row: int = row
        self.col = col
        self.visited = False
        self.north = True
        self.south = True
        self.east = True
        self.west = True
        self.hexa = 0
