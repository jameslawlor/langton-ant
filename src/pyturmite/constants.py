CANVAS_SIZE = 8
N_STEPS = 8342
PLOT_MODE = "animate"
CMAP = "Oranges"
# RULESET = "classic"  # 'classic' or 'stateful'
# INSTRUCTIONS = "RCCU"
RULESET = 'stateful'
INSTRUCTIONS = [                    # triplet notation (write colour, turn instruction, next state)
    [(1, 'R', 0),(1, 'R', 1)],     # one state per row, one colour per tuple
    [(0, 'N', 0),(0, 'N', 1)],
]
ANIMATION_INTERVAL = 1
PADDING_SIZE = 2  # expand in each direction by this amount of cells
SAVE_ANIMATION = False
FRAME_SKIP = 1
