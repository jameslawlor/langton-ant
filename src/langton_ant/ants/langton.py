import numpy as np
import matplotlib.pylab as plt
from langton_ant.constants import CMAP, RULESET
"""
The colors are modified in a cyclic fashion. 
A simple naming scheme is used: for each of the successive colors, 
a letter "L" or "R" is used to indicate whether a left or right turn 
should be taken. 
Langton's ant has the name "RL" in this naming scheme.
"""

class LangtonAnt:
    def __init__(
        self,
        x0=0,
        y0=0,
        dir0="u",
        ruleset=RULESET,
    ):
        self.x = x0
        self.y = y0
        self.dir = dir0
        self.parse_ruleset(ruleset)

    def __str__(self):
        return str(vars(self))
    
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

    def rule_to_func(self, rule):
        if rule == "R":
            return self.turn_clockwise
        elif rule =="L":
            return self.turn_counter_clockwise        


    def parse_ruleset(self, ruleset):
        # TODO: Check validity
        
        self.cmap = plt.get_cmap(CMAP)
        colours= self.cmap(
            np.linspace(.0, 1, len(ruleset))
        )

        self.rules = {}

        for ix, rule in enumerate(ruleset):
            self.rules[ix] = {
                "colour": colours[ix],
                "instruction": self.rule_to_func(rule),
        }
            
        self.n_colours = len(colours)
        

    def init_grid(self, canvas_size, offset=True):

        if offset:
            self.x = self.x + int(canvas_size / 2)
            self.y = self.y + int(canvas_size / 2)
            
        self.grid = np.zeros((canvas_size, canvas_size))


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
        return self.grid[i, j]


    def change_colour(self, i, j):
        self.grid[i, j] = (self.grid[i, j] + 1) % self.n_colours


    def turn(self, colour):
        turn_instruction = self.rules[colour]["instruction"]
        turn_instruction()


    def update(self):
        colour = self.check_square_colour(self.x, self.y)
        self.turn(colour)
        self.change_colour(self.x, self.y)
        self.move()
