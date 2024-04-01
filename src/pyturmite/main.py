from pyturmite.turmites import ClassicTurmite, StatefulTurmite
from pyturmite.utils.plotters import Plotter
from pyturmite.utils.input_handling import parse_args


def main():
    args = parse_args()
    if args.ruleset == "classic":
        turmite = ClassicTurmite()
    elif args.ruleset == "stateful":
        turmite = StatefulTurmite()

    turmite.init_grid(canvas_size=args.canvas_size)
    plotter = Plotter(mode=args.plot_mode)
    plotter.plot(turmite=turmite, n_steps=args.n_steps)


if __name__ == "__main__":
    main()
