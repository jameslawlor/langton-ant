from langton_ant.ants.langton import LangtonAnt
from langton_ant.utils.plotters import Plotter
from langton_ant.utils.input_handling import parse_args


def main():
    args = parse_args()
    ant = LangtonAnt()

    ant.init_grid(canvas_size=args.canvas_size)

    plotter = Plotter()
    plotter.plot(ant=ant, n_steps=args.n_steps, mode=args.plot_mode)


if __name__ == "__main__":
    main()
