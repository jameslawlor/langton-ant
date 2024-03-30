from pyturmite.turmites import Turmite
from pyturmite.utils.plotters import Plotter
from pyturmite.utils.input_handling import parse_args


def main():
    args = parse_args()
    turmite = Turmite()

    turmite.init_grid(canvas_size=args.canvas_size)

    plotter = Plotter()
    plotter.plot(turmite=turmite, n_steps=args.n_steps, mode=args.plot_mode)


if __name__ == "__main__":
    main()
