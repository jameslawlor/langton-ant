# TODO - make a base class for all lattices
# TODO - add coord translation to non-negative quadrant to base class, so all child lattice classes can inherit it

class SquareLattice:
    def __init__(
        self,
    ):
        self.black_squares = []

    def check_square_colour(self, x,y):
        if (x,y) in self.black_squares:
            return "black"
        else:
            return "white"
        
    def change_colour(self, x, y):
        if (x,y) in self.black_squares:
            self.black_squares.remove((x,y))
        else:
            self.black_squares.append((x,y))

    def find_grid_boundaries(self):
        if self.black_squares:
            min_x = min([x for (x,y) in self.black_squares])
            max_x = max([x for (x,y) in self.black_squares])
            min_y = min([y for (x,y) in self.black_squares])
            max_y = max([y for (x,y) in self.black_squares])

            return (min_x, max_x, min_y, max_y)
        
        else:
            return (None, None, None, None)
