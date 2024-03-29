from langton_ant.ants.langton import LangtonAnt
from langton_ant.utils.plotters import Plotter

CANVAS_SIZE = 128
N_STEPS = 11000
PLOT_MODE = "animate"


def main():
    ant = LangtonAnt()

    ant.init_grid(canvas_size=CANVAS_SIZE)

    plotter = Plotter()
    plotter.plot(ant=ant, n_steps=N_STEPS, mode=PLOT_MODE)


if __name__ == "__main__":
    main()
