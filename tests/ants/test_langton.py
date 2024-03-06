import pytest
from langton_ant.ants.langton import LangtonAnt

import unittest

class LangtonAntTest(unittest.TestCase):

    def test_initial_state(self):
        """
        Tests the initial state of the Langton ant.
        """
        ant = LangtonAnt()
        self.assertEqual(ant.x, 0)
        self.assertEqual(ant.y, 0)
        self.assertEqual(ant.dir, "u")

    def test_turn_clockwise(self):
        """
        Tests turning the ant clockwise.
        """
        ant = LangtonAnt()

        # Up -> Right
        ant.turn_clockwise()
        self.assertEqual(ant.dir, "r")

        # Right -> Down
        ant.turn_clockwise()
        self.assertEqual(ant.dir, "d")

        # Down -> Left
        ant.turn_clockwise()
        self.assertEqual(ant.dir, "l")

        # Left -> Up (wrap around)
        ant.turn_clockwise()
        self.assertEqual(ant.dir, "u")

    def test_turn_counter_clockwise(self):
        """
        Tests turning the ant counter-clockwise.
        """
        ant = LangtonAnt()

        # Up -> Left
        ant.turn_counter_clockwise()
        self.assertEqual(ant.dir, "l")

        # Left -> Down
        ant.turn_counter_clockwise()
        self.assertEqual(ant.dir, "d")

        # Down -> Right
        ant.turn_counter_clockwise()
        self.assertEqual(ant.dir, "r")

        # Right -> Up (wrap around)
        ant.turn_counter_clockwise()
        self.assertEqual(ant.dir, "u")

    def test_move_up(self):
        """
        Tests moving the ant upwards.
        """
        ant = LangtonAnt()
        ant.dir = "u"
        ant.move()
        self.assertEqual(ant.x, 0)
        self.assertEqual(ant.y, 1)

    def test_move_down(self):
        """
        Tests moving the ant downwards.
        """
        ant = LangtonAnt()
        ant.dir = "d"
        ant.move()
        self.assertEqual(ant.x, 0)
        self.assertEqual(ant.y, -1)

    def test_move_left(self):
        """
        Tests moving the ant left.
        """
        ant = LangtonAnt()
        ant.dir = "l"
        ant.move()
        self.assertEqual(ant.x, -1)
        self.assertEqual(ant.y, 0)

    def test_move_right(self):
        """
        Tests moving the ant right.
        """
        ant = LangtonAnt()
        ant.dir = "r"
        ant.move()
        self.assertEqual(ant.x, 1)
        self.assertEqual(ant.y, 0)

if __name__ == "__main__":
    unittest.main()