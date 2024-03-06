import matplotlib.pylab as plt

class Lattice:
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
            # print("pop ", x, y)
            self.black_squares.remove((x,y))
            # print(self.black_squares)
        else:
            self.black_squares.append((x,y))
            # print("append ", self.black_squares)

    def find_grid_boundaries(self):
        min_x = min([x for (x,y) in self.black_squares])
        max_x = max([x for (x,y) in self.black_squares])
        min_y = min([y for (x,y) in self.black_squares])
        max_y = max([y for (x,y) in self.black_squares])

        return (min_x, max_x, min_y, max_y)


class Ant:    
    def __init__(
        self,
    ):
        self.x = 0
        self.y = 0
        self.dir = "u"

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

import numpy as np

def plot_grid(boundaries, black_squares):
    """
    Plots a square grid with black and white squares based on a list of coordinates.

    Args:
    grid_size: The size of the grid (number of squares in a row and column).
    black_squares: A list of tuples representing coordinates (x, y) of black squares.
    """
    # Create a figure and axis
    fig, ax = plt.subplots()

    x_buffer = 2
    y_buffer = 2

    # translate
    (min_x, max_x, min_y, max_y) = boundaries
    if min_x < 0:
        x_offset = abs(min_x) 
    if min_y < 0:
        y_offset = abs(min_y)

    black_squares_translated = []

    for (x,y) in black_squares:
        x_shifted = x + x_offset
        y_shifted = y + y_offset
        black_squares_translated.append((x_shifted, y_shifted))

    x_size = max_x + x_offset + 1
    y_size = max_y + y_offset + 1

    # Generate data for the grid (each square is a unit square)
    data = np.zeros((y_size, x_size))

    print(black_squares_translated)

    # # Mark black squares based on coordinates
    for (x, y) in black_squares_translated:
        data[y, x] = 1  # Index convention: y, x for rows and columns

    # Set axis limits based on grid size
    ax.set_xlim(0, x_size)
    ax.set_ylim(0, y_size)

    # Turn off axis labels and ticks for a clean grid
    ax.axis('off')

    # Create a colormap with black and white
    cmap = "Greys"# ['white', 'black']

    # print(data)
    # Plot the grid using pcolormesh with the colormap
    ax.pcolormesh(data, cmap=cmap)

    # Show the plot
    plt.show()


def main():
    ant = Ant()
    grid = Lattice()
    
    for step in range(20000):
        x_pos = ant.x
        y_pos = ant.y
        colour = grid.check_square_colour(x_pos, y_pos)
        
        if colour == "white":
            ant.turn_clockwise()

        elif colour == "black":
            ant.turn_counter_clockwise()

        grid.change_colour(x_pos, y_pos)
        ant.move()

    boundaries = grid.find_grid_boundaries()

    plot_grid(boundaries, grid.black_squares)


if __name__ == "__main__":
    main()