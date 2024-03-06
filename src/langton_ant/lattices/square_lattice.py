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

    def get_y_min(self):
        return min([y for (_,y) in self.black_squares])
    
    def get_y_max(self):
        return max([y for (_,y) in self.black_squares])

    def get_x_min(self):
        return min([x for (x,_) in self.black_squares])
    
    def get_x_max(self):
        return max([x for (x,_) in self.black_squares])

    def translate_to_positive_quadrant(self):
        """
        coordinate shift all black squares
        to +ive quadrant for plotting 
        """
        if self.get_x_min() < 0:
            self.x_offset = abs(self.get_x_min())
        else:
            self.x_offset = 0
        
        if self.get_y_min() < 0:
            self.y_offset = abs(self.get_y_min())
        else:
            self.y_offset = 0

        translated_squares = []

        for (x,y) in self.black_squares:
            x_shifted = x + self.x_offset
            y_shifted = y + self.y_offset
            translated_squares.append((x_shifted, y_shifted))

        self.black_squares = translated_squares
