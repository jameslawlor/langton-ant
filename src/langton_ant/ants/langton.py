import numpy as np


class LangtonAnt:
    def __init__(
        self,
        x0=0,
        y0=0,
        dir0="u",
    ):
        self.x = x0
        self.y = y0
        self.dir = dir0

    def __str__(self):
        return str(vars(self))
    
    def init_grid(self, canvas_size, offset=True):

        if offset:
            self.x = self.x + int(canvas_size / 2)
            self.y = self.y + int(canvas_size / 2)
            
        self.grid = np.zeros((canvas_size, canvas_size))


    def turn_clockwise(self):
        if self.dir == "u":
            self.dir = "r"
        elif self.dir == "r":
            self.dir = "d"
        elif self.dir == "d":
            self.dir = "l"
        elif self.dir == "l":
            self.dir = "u"

    def turn_counter_clockwise(self):
        if self.dir == "u":
            self.dir = "l"
        elif self.dir == "l":
            self.dir = "d"
        elif self.dir == "d":
            self.dir = "r"
        elif self.dir == "r":
            self.dir = "u"

    def move(self):
        if self.dir == "u":
            self.y += 1
        elif self.dir == "l":
            self.x -= 1
        elif self.dir == "d":
            self.y -= 1
        elif self.dir == "r":
            self.x += 1

    def check_square_colour(self, i, j):
        if self.grid[i, j] == 0:
            return "white"
        else:
            return "black"

    def change_colour(self, i, j):
        if self.grid[i, j] == 0:
            self.grid[i, j] = 1
        else:
            self.grid[i, j] = 0

    def update(self):
        colour = self.check_square_colour(self.x, self.y)

        if colour == "white":
            self.turn_clockwise()

        elif colour == "black":
            self.turn_counter_clockwise()

        self.change_colour(self.x, self.y)
        self.move()
