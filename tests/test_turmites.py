from pyturmite.turmites import Turmite, Direction
import pytest


def test_initial_state():
    """
    Tests the initial state of the turmite
    """
    turmite = Turmite()
    assert turmite.x == 0
    assert turmite.y == 0
    assert turmite.dir == Direction.U


@pytest.mark.parametrize(
    "input_direction,expected_output",
    [
        (Direction.U, Direction.R),  # Up -> Right
        (Direction.R, Direction.D),  # Right -> Down
        (Direction.D, Direction.L),  # Down -> Left
        (Direction.L, Direction.U),  # Left -> Up
    ],
)
def test_turn_clockwise(input_direction, expected_output):
    """
    Tests turning the turmite clockwise.
    """
    turmite = Turmite()
    turmite.dir = input_direction
    turmite.turn_clockwise()
    assert turmite.dir == expected_output


@pytest.mark.parametrize(
    "input_direction,expected_output",
    [
        (Direction.R, Direction.U),  # Right -> Up
        (Direction.D, Direction.R),  # Down -> Right
        (Direction.L, Direction.D),  # Left -> Down
        (Direction.U, Direction.L),  # Up -> Left
    ],
)
def test_turn_counter_clockwise(input_direction, expected_output):
    """
    Tests turning the turmite counter-clockwise.
    """
    turmite = Turmite()
    turmite.dir = input_direction
    turmite.turn_counter_clockwise()
    assert turmite.dir == expected_output


@pytest.mark.parametrize(
    "move_direction,expected_output",
    [
        (Direction.U, (0, 1)),
        (Direction.R, (1, 0)),
        (Direction.D, (0, -1)),
        (Direction.L, (-1, 0)),
    ],
)
def test_movement(move_direction, expected_output):
    """
    Tests moving the turmite
    """

    turmite = Turmite()
    turmite.dir = move_direction
    turmite.move()
    assert (turmite.x, turmite.y) == expected_output


def test_init_grid():
    """
    Test grid initialisation
    """
    turmite = Turmite()
    turmite.init_grid(canvas_size=4)
    assert (turmite.x, turmite.y) == (2, 2)


def test_init_grid_no_offset():
    """
    Test grid initialisation without offseting turmite position
    """
    turmite = Turmite()
    turmite.init_grid(canvas_size=4, offset=False)
    assert (turmite.x, turmite.y) == (0, 0)
