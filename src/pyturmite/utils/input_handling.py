import argparse
from pyturmite.constants import (
    CANVAS_SIZE,
    N_STEPS,
    PLOT_MODE,
    RULESET,
)


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--n_steps", required=False, type=int, default=N_STEPS)

    parser.add_argument("--canvas_size", required=False, type=int, default=CANVAS_SIZE)

    parser.add_argument("--plot_mode", required=False, type=str, default=PLOT_MODE)

    parser.add_argument("--ruleset", required=False, type=str, default=RULESET)

    args = parser.parse_args()
    return args
