import numpy as np
import matplotlib.pylab as plt
from pyturmite.constants import CMAP, RULESET, PADDING_SIZE, INSTRUCTIONS

"""
The colors are modified in a cyclic fashion. 
A simple naming scheme is used: for each of the successive colors, 
a letter "L" or "R" is used to indicate whether a left or right turn 
should be taken. 
Langton's turmite has the name "RL" in this naming scheme.
"""


class Turmite:
    def __init__(
        self,
        x0=0,
        y0=0,
        dir0="u",
        ruleset=RULESET,
        instructions=INSTRUCTIONS,
    ):
        self.x = x0
        self.y = y0
        self.dir = dir0
        self.ruleset = ruleset

        if ruleset == "classic":
            self.parse_classic_instruction_input(instructions)
        elif ruleset == "stateful":
            self.parse_stateful_instruction_input(instructions)
            self.state = 0 # TODO: Get from input instructions instead

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

    def make_u_turn(self):
        if self.dir == "u":
            self.dir = "d"
        elif self.dir == "l":
            self.dir = "r"
        elif self.dir == "d":
            self.dir = "u"
        elif self.dir == "r":
            self.dir = "l"

    def no_turn(self):
        pass

    def instruction_to_func(self, instruction):
        if instruction == "R":
            return self.turn_clockwise
        elif instruction == "L":
            return self.turn_counter_clockwise
        elif instruction == "U" or instruction == "B":
            return self.make_u_turn
        elif instruction == "C" or instruction == "F" or instruction == "N":
            return self.no_turn
        else:
            raise ValueError(f"Instruction {instruction} not recognised! Check inputs!")

    def parse_classic_instruction_input(self, instructions):
        # TODO: Check validity

        self.cmap = plt.get_cmap(CMAP)
        colours = self.cmap(np.linspace(0.0, 1, len(instructions)))

        self.instructions = {}

        for ix, instruction in enumerate(instructions):
            self.instructions[ix] = {
                "colour": colours[ix],
                "instruction": self.instruction_to_func(instruction),
            }

        self.n_colours = len(colours)

    def parse_stateful_instruction_input(self, input_instructions):
        """
        row = state
        col = colour
        """
        # TODO: Check validity
        self.cmap = plt.get_cmap(CMAP)
        colours = self.cmap(np.linspace(0.0, 1, len(input_instructions[0])))
        self.n_colours = len(colours)
        self.n_states = len(input_instructions)
        self.instructions_stateful = np.array(input_instructions)

    def init_grid(self, canvas_size, offset=True):
        if offset:
            self.x = self.x + int(canvas_size / 2)
            self.y = self.y + int(canvas_size / 2)

        self.grid = np.zeros((canvas_size, canvas_size), dtype=int)

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
        return int(self.grid[i, j])

    def change_colour(self, i, j):
        self.grid[i, j] = (self.grid[i, j] + 1) % self.n_colours

    def turn_classic(self, colour):
        turn_instruction = self.instructions[colour]["instruction"]
        turn_instruction()

    def turn_stateful(self, colour, state):
        colour_state_tuple = self.instructions_stateful[state][colour]
        
        # change state
        self.state = int(colour_state_tuple[-1])
        # change colour
        colour_to_write = int(colour_state_tuple[0])
        self.grid[self.x, self.y] = colour_to_write
        print(colour, state, colour_state_tuple, colour_to_write, self.state)
        # move instruction
        instruction = colour_state_tuple[1]
        self.instruction_to_func(instruction)()

    def update(self):
        if self.ruleset == "classic":
            colour = self.check_square_colour(self.x, self.y)
            self.turn_classic(colour)
            self.change_colour(self.x, self.y)
            self.move()

        elif self.ruleset == "stateful":
            colour = self.check_square_colour(self.x, self.y)
            self.turn_stateful(colour, self.state)
            self.move()

        # expand canvas/grid if we moved outside it
        if (
            (self.x >= self.grid.shape[0])
            or (self.x < 0)
            or (self.y >= self.grid.shape[1])
            or (self.y < 0)
        ):
            self.expand_grid()

    def expand_grid(self):
        self.grid = np.pad(self.grid, PADDING_SIZE)
        self.x += PADDING_SIZE
        self.y += PADDING_SIZE
