import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation
from functools import partial
import numpy as np

from pyturmite.constants import ANIMATION_INTERVAL, SAVE_ANIMATION, FRAME_SKIP


class Plotter:
    def __init__(self):
        self.turmite = None

    def plot(self, turmite, n_steps, mode):
        if mode == "static":
            self.static_plot(turmite, n_steps)

        elif mode == "animate":
            self.animate(turmite, n_steps)

    def static_plot(
        self,
        turmite,
        N_STEPS,
    ):
        for _ in range(N_STEPS):
            turmite.update()

        data = np.array(turmite.grid)
        data[turmite.x][turmite.y] = turmite.n_colours + 1
        plt.figure()
        plt.imshow(
            data,
            interpolation="none",
            vmin=0,
            vmax=turmite.n_colours + 1,
            cmap=turmite.cmap,
        )
        plt.show()

    def animate(self, turmite, n_steps):
        fig = plt.figure()

        im = plt.imshow(
            turmite.grid,
            interpolation="none",
            vmin=0,
            vmax=turmite.n_colours + 1,
            cmap=turmite.cmap,
        )
        ax = plt.gca()
        frame_num = ax.text(
            0.99,
            0.01,
            "",
            fontsize=5,
            horizontalalignment="right",
            verticalalignment="bottom",
            transform=ax.transAxes,
        )
        frame_num.set_bbox(
            dict(facecolor="white", alpha=0.3, edgecolor="black", lw=0.1)
        )
        plt.axis("off")

        def update(step, turmite, skip=FRAME_SKIP):
            for _ in range(skip):
                turmite.update()
            data = np.array(turmite.grid)
            data[turmite.x][turmite.y] = turmite.n_colours + 1
            im.set_data(data)
            frame_num.set_text(f"Step: {step*skip:,}")
            return [im, frame_num]

        anim = FuncAnimation(  # noqa: F841
            fig,
            partial(
                update,
                turmite=turmite,
            ),
            frames=n_steps,
            interval=ANIMATION_INTERVAL,
            blit=True,
            repeat=False,
        )

        if SAVE_ANIMATION:
            anim.save(
                "example.mp4",
                writer="ffmpeg",
                fps=120,
                progress_callback=lambda i, n: print(f"Saving frame {i}/{n}"),
            )

        plt.show()
