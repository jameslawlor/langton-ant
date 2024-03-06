from langton_ant.ants.langton import LangtonAnt
from langton_ant.lattices.square_lattice import SquareLattice
from langton_ant.utils.plotters import plot

def main():
    ant = LangtonAnt()
    grid = SquareLattice()
    
    for step in range(11500):
        x_pos = ant.x
        y_pos = ant.y
        colour = grid.check_square_colour(x_pos, y_pos)
        
        if colour == "white":
            ant.turn_clockwise()

        elif colour == "black":
            ant.turn_counter_clockwise()

        grid.change_colour(x_pos, y_pos)
        ant.move()

    grid.translate_to_positive_quadrant()

    ant.translate(x_offset=grid.x_offset, y_offset=grid.y_offset)

    plot(grid, ant)


if __name__ == "__main__":
    main()