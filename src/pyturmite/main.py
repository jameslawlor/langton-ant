from pyturmite.turmites import ClassicTurmite, StatefulTurmite
from pyturmite.utils.plotters import Plotter
from pyturmite.utils.input_handling import Config


def main():
    config = Config()
    config.load()

    print(config)

    if config.ruleset == "classic":
        turmite = ClassicTurmite()
    elif config.ruleset == "stateful":
        turmite = StatefulTurmite()

    turmite.init_grid(
        canvas_size=config.canvas_size,
    )
    turmite.load(
        instructions=config.instructions,
        padding_size=config.padding_size,
        ruleset=config.ruleset,
        cmap_str=config.cmap,
    )

    plotter = Plotter(
        mode=config.plot_mode,
        animation_interval=config.animation_interval,
        save_animation=config.save_animation,
        frame_skip=config.frame_skip,
    )
    plotter.plot(
        turmite=turmite,
        n_steps=config.n_steps,
    )


if __name__ == "__main__":
    main()
