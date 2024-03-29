import matplotlib.pylab as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from functools import partial
from langton_ant.constants import CMAP, ANIMATION_INTERVAL

class Plotter:
    def __init__(self):
        self.ant = None

    def plot(self, ant, n_steps, mode):
        if mode == "static":
            self.static_plot(ant, n_steps)

        elif mode == "animate":
            self.animate(ant, n_steps)

    def static_plot(
        self,
        ant,
        N_STEPS,
    ):
        for _ in range(N_STEPS):
            ant.update()

        data = np.array(ant.grid)
        data[ant.x][ant.y] = 2
        plt.figure()
        plt.imshow(
            data,
            interpolation="none",
            vmin=0,
            vmax=2,
            cmap=CMAP,
        )
        plt.show()

    def animate(self, ant, n_steps):

        fig = plt.figure()
        im = plt.imshow(
            ant.grid,
            interpolation="none",
            vmin=0,
            vmax=ant.n_colours+1,
            cmap=ant.cmap,
        )

        def update(step, ant):
            ant.update()
            data = np.array(ant.grid)
            data[ant.x][ant.y] = ant.n_colours+1
            im.set_data(data)
            return [im]

        anim = FuncAnimation(  # noqa: F841
            fig,
            partial(update, ant=ant),
            frames=n_steps,
            interval=ANIMATION_INTERVAL,
            blit=True,
            repeat=False,
        )

        plt.show()
