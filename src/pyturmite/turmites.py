import numpy as np
import matplotlib.pylab as plt
from pyturmite.constants import (
    CMAP,
    RULESET,
    PADDING_SIZE,
    INSTRUCTIONS,
)


class Direction:
    U = "u"
    R = "r"
    D = "d"
    L = "l"


class Turmite:
    """
    Base class for all Turmites
    """

    def __init__(
        self,
        x0=0,
        y0=0,
        initial_direction=Direction.U,
        instructions=INSTRUCTIONS,
        ruleset=RULESET,
    ):
        self.x = x0
        self.y = y0
        self.dir = initial_direction
        self.ruleset = ruleset
        self.cmap = plt.get_cmap(CMAP)
        self.n_colours = 0
        self.parse_instructions(instructions)
        self.movement_history = []
        self.colour_history = []

    def __str__(self):
        return str(vars(self))

    def turn_clockwise(self):
        if self.dir == Direction.U:
            self.dir = Direction.R
        elif self.dir == Direction.R:
            self.dir = Direction.D
        elif self.dir == Direction.D:
            self.dir = Direction.L
        elif self.dir == Direction.L:
            self.dir = Direction.U

    def turn_counter_clockwise(self):
        if self.dir == Direction.U:
            self.dir = Direction.L
        elif self.dir == Direction.L:
            self.dir = Direction.D
        elif self.dir == Direction.D:
            self.dir = Direction.R
        elif self.dir == Direction.R:
            self.dir = Direction.U

    def make_u_turn(self):
        if self.dir == Direction.U:
            self.dir = Direction.D
        elif self.dir == Direction.L:
            self.dir = Direction.R
        elif self.dir == Direction.D:
            self.dir = Direction.U
        elif self.dir == Direction.R:
            self.dir = Direction.L

    def no_turn(self):
        pass

    def instruction_to_func(self, instruction):
        if instruction == "R":
            return self.turn_clockwise
        elif instruction == "L":
            return self.turn_counter_clockwise
        elif instruction in ("U", "B"):
            return self.make_u_turn
        elif instruction in ("C", "F", "N"):
            return self.no_turn
        else:
            raise ValueError(f"Instruction {instruction} not recognised! Check inputs!")

    def init_grid(self, canvas_size, offset=True):
        if offset:
            self.x = self.x + int(canvas_size / 2)
            self.y = self.y + int(canvas_size / 2)

        self.grid = np.zeros((canvas_size, canvas_size), dtype=int)

    def move(self):
        if self.dir == Direction.U:
            self.y += 1
        elif self.dir == Direction.L:
            self.x -= 1
        elif self.dir == Direction.D:
            self.y -= 1
        elif self.dir == Direction.R:
            self.x += 1

    def check_square_colour(self, i, j):
        return int(self.grid[i, j])

    def change_colour(self, i, j):
        self.grid[i, j] = (self.grid[i, j] + 1) % self.n_colours

    def expand_grid(self):
        """
        Expands the background canvas/grid if turmite moved outside it
        """
        if (
            (self.x >= self.grid.shape[0])
            or (self.x < 0)
            or (self.y >= self.grid.shape[1])
            or (self.y < 0)
        ):
            self.grid = np.pad(self.grid, PADDING_SIZE)
            self.x += PADDING_SIZE
            self.y += PADDING_SIZE

    def update(self):
        raise NotImplementedError(
            "update method not implemented in base turmite class!"
        )

    def parse_instructions(self, *args):
        pass

    def turn(self, *args):
        raise NotImplementedError("turn method not implemented in base turmite class!")


class ClassicTurmite(Turmite):
    """
    'Classic' instruction set e.g. Langton's Ant

    https://en.wikipedia.org/wiki/Langton%27s_ant
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def parse_instructions(self, instructions):
        colours = self.cmap(np.linspace(0.0, 1, len(instructions)))
        self.n_colours = len(colours)

        self.colour_to_instruction_mappings = {
            ix: {
                "colour": colours[ix],
                "instruction": instruction,
                "instruction_function": self.instruction_to_func(instruction),
            }
            for ix, instruction in enumerate(instructions)
        }

    def turn(self, colour):
        self.colour_history.append(colour)

        colour_to_instruction_mapping = self.colour_to_instruction_mappings[colour]
        instruction = colour_to_instruction_mapping["instruction"]
        self.movement_history.append(instruction)
        turn_instruction_function = colour_to_instruction_mapping[
            "instruction_function"
        ]
        turn_instruction_function()

    def update(self):
        colour = self.check_square_colour(self.x, self.y)
        self.turn(colour)
        self.change_colour(self.x, self.y)
        self.move()
        self.expand_grid()


class StatefulTurmite(Turmite):
    """
    Uses state/colour/turn/move notation
    from https://en.wikipedia.org/wiki/Turmite#Specification
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = 0

    def parse_instructions(self, input_instructions):
        """
        row = state
        col = colour
        """
        # TODO: Check validity
        self.cmap = plt.get_cmap(CMAP)
        colours = self.cmap(np.linspace(0.0, 1, len(input_instructions[0])))
        self.n_colours = len(colours)
        self.n_states = len(input_instructions)
        self.instruction_mappings = np.array(input_instructions)

    def turn(self, colour, state):
        colour_state_tuple = self.instruction_mappings[state][colour]

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
        colour = self.check_square_colour(self.x, self.y)
        self.turn(colour, self.state)
        self.move()
        self.expand_grid()
