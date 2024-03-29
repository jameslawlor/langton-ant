import matplotlib.pylab as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from functools import partial
from matplotlib.colors import ListedColormap

cmap = ListedColormap(["white", "black", "red"])

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
            cmap=cmap,
        )
        plt.show()


    def animate(self, ant, n_steps):

        INTERVAL = 0

        fig = plt.figure()
        im = plt.imshow(
            ant.grid,
            interpolation="none",
            vmin=0,
            vmax=2,
            cmap=cmap,
        )

        def update(step, ant):
            ant.update()
            data = np.array(ant.grid)
            data[ant.x][ant.y] = 2
            im.set_data(data)
            return [im]

        anim = FuncAnimation(
            fig,
            partial(update, ant=ant),
            frames=n_steps,
            interval=INTERVAL,
            blit=True,
            repeat=False,
        )

        plt.show()
