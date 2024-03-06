import matplotlib.pylab as plt
import numpy as np

def set_ax_ticks(
        ax,
        x_size,
        y_size,
        ):
    
    ax.set_xlim(0, x_size)
    ax.set_ylim(0, y_size)

    # Turn off axis labels and ticks for a clean grid
    # ax.axis('off') 

    # TODO - ugh, also horrible
    major_xticks = range(0, x_size, 10)
    major_yticks = range(0, y_size, 10)
    minor_xticks = range(0, x_size, 1)
    minor_yticks = range(0, y_size, 1)

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

    return ax

def plot(
        lattice,
        ant,
    ):
    """
    Plots a square grid with black and white squares.
    """
    fig, ax = plt.subplots()

    # Set axis limits based on grid size
    x_size = lattice.get_x_max()
    y_size = lattice.get_y_max()

    # Generate data for the grid (each square is a unit square)
    data = np.zeros((y_size+1, x_size+1))
    # # Mark black squares based on coordinates
    for (x, y) in lattice.black_squares:
        data[y, x] = 1

    data[ant.y,ant.x] = 2

    # ax = set_ax_ticks(ax, x_size, y_size)
    # ax.grid(True, 
    #         which='both', 
    #         axis='both', 
    #         linestyle='-', 
    #         color='k')
    
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap(['white', 'black', 'red'])

    # ax.pcolormesh(data, cmap=cmap)
    ax.imshow(data,
              cmap=cmap,
              origin='upper',
              )
    
    plt.show()