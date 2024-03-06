import unittest
from langton_ant.lattices.square_lattice import SquareLattice

class SquareLatticeTest(unittest.TestCase):

    def test_initial_state(self):
        """
        Tests the initial state of the SquareLattice.
        """
        lattice = SquareLattice()
        self.assertEqual(lattice.black_squares, [])

    def test_check_square_colour_black(self):
        """
        Tests checking the color of a black square.
        """
        lattice = SquareLattice()
        lattice.black_squares.append((1, 2))
        self.assertEqual(lattice.check_square_colour(1, 2), "black")

    def test_check_square_colour_white(self):
        """
        Tests checking the color of a white square.
        """
        lattice = SquareLattice()
        lattice.black_squares.append((1, 2))
        self.assertEqual(lattice.check_square_colour(0, 0), "white")

    def test_change_colour_to_black(self):
        """
        Tests changing the color of a white square to black.
        """
        lattice = SquareLattice()
        lattice.change_colour(1, 2)
        self.assertEqual(lattice.black_squares, [(1, 2)])

    def test_change_colour_to_white(self):
        """
        Tests changing the color of a black square to white.
        """
        lattice = SquareLattice()
        lattice.black_squares.append((1, 2))
        lattice.change_colour(1, 2)
        self.assertEqual(lattice.black_squares, [])

    def test_find_grid_boundaries_empty(self):
        """
        Tests finding grid boundaries for an empty lattice.
        """
        lattice = SquareLattice()
        self.assertEqual(lattice.find_grid_boundaries(), (None, None, None, None))

    def test_find_grid_boundaries_with_squares(self):
        """
        Tests finding grid boundaries with black squares.
        """
        lattice = SquareLattice()
        lattice.black_squares.append((-1, 3))
        lattice.black_squares.append((2, -2))
        self.assertEqual(lattice.find_grid_boundaries(), (-1, 2, -2, 3))

if __name__ == "__main__":
    unittest.main()
