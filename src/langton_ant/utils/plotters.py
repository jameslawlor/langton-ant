import matplotlib.pylab as plt
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

    # This is ugly, fix it
    (min_x, max_x, min_y, max_y) = boundaries
    
    if min_x < 0:
        x_offset = abs(min_x) 
    if min_y < 0:
        y_offset = abs(min_y)

    # TODO - shift this to the lattice class
    black_squares_translated = []

    for (x,y) in black_squares:
        x_shifted = x + x_offset
        y_shifted = y + y_offset
        black_squares_translated.append((x_shifted, y_shifted))

    x_size = max_x + x_offset + 1
    y_size = max_y + y_offset + 1

    # Generate data for the grid (each square is a unit square)
    data = np.zeros((x_size, y_size))

    # TODO - this is ugly, fix it
    min_x = min([x for (x,y) in black_squares_translated])
    max_x = max([x for (x,y) in black_squares_translated])
    min_y = min([y for (x,y) in black_squares_translated])
    max_y = max([y for (x,y) in black_squares_translated])

    # # Mark black squares based on coordinates
    for (x, y) in black_squares_translated:
        print(x, y)
        data[x, y] = 1  # Index convention: y, x for rows and columns

    print(x_size, y_size)
    # Set axis limits based on grid size
    ax.set_xlim(0, y_size)
    ax.set_ylim(0, x_size)

    # Turn off axis labels and ticks for a clean grid
    # ax.axis('off') 

    # TODO - ugh, also horrible
    major_xticks = range(0, y_size, 10)
    major_yticks = range(0, x_size, 10)
    minor_xticks = range(0, y_size, 1)

    # I want minor ticks for y axis
    minor_yticks = range(0, x_size, 1)

    ax.set_xticks(major_xticks)
    ax.set_xticks(minor_xticks, minor = True)

    ax.set_yticks(major_yticks)
    ax.set_yticks(minor_yticks, minor = True)
    # Specify tick label size
    ax.tick_params(axis = 'both', which = 'major', labelsize = 6)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 0)
    
    ax.set_xticks(major_xticks)
    ax.set_xticks(minor_xticks, minor = True)

    ax.set_yticks(major_yticks)
    ax.set_yticks(minor_yticks, minor = True)

    # Set both ticks to be outside
    ax.tick_params(which = 'both', direction = 'out')

    # Specify different settings for major and minor grids
    ax.grid(which = 'minor', alpha = 0.1)
    ax.grid(which = 'major', alpha = 0.3)

    ax.grid(True, 
            which='both', 
            axis='both', 
            linestyle='-', 
            color='k')
    cmap = "Greys"
    ax.pcolormesh(data, cmap=cmap)
    plt.show()