from pyturmite.turmites import Turmite

import unittest


class TurmiteTest(unittest.TestCase):
    def test_initial_state(self):
        """
        Tests the initial state of the turmite
        """
        turmite = Turmite()
        self.assertEqual(turmite.x, 0)
        self.assertEqual(turmite.y, 0)
        self.assertEqual(turmite.dir, "u")

    def test_turn_clockwise(self):
        """
        Tests turning the turmite clockwise.
        """
        turmite = Turmite()

        # Up -> Right
        turmite.turn_clockwise()
        self.assertEqual(turmite.dir, "r")

        # Right -> Down
        turmite.turn_clockwise()
        self.assertEqual(turmite.dir, "d")

        # Down -> Left
        turmite.turn_clockwise()
        self.assertEqual(turmite.dir, "l")

        # Left -> Up (wrap around)
        turmite.turn_clockwise()
        self.assertEqual(turmite.dir, "u")

    def test_turn_counter_clockwise(self):
        """
        Tests turning the turmite counter-clockwise.
        """
        turmite = Turmite()

        # Up -> Left
        turmite.turn_counter_clockwise()
        self.assertEqual(turmite.dir, "l")

        # Left -> Down
        turmite.turn_counter_clockwise()
        self.assertEqual(turmite.dir, "d")

        # Down -> Right
        turmite.turn_counter_clockwise()
        self.assertEqual(turmite.dir, "r")

        # Right -> Up (wrap around)
        turmite.turn_counter_clockwise()
        self.assertEqual(turmite.dir, "u")

    def test_move_up(self):
        """
        Tests moving the turmite upwards.
        """
        turmite = Turmite()
        turmite.dir = "u"
        turmite.move()
        self.assertEqual(turmite.x, 0)
        self.assertEqual(turmite.y, 1)

    def test_move_down(self):
        """
        Tests moving the turmite downwards.
        """
        turmite = Turmite()
        turmite.dir = "d"
        turmite.move()
        self.assertEqual(turmite.x, 0)
        self.assertEqual(turmite.y, -1)

    def test_move_left(self):
        """
        Tests moving the turmite left.
        """
        turmite = Turmite()
        turmite.dir = "l"
        turmite.move()
        self.assertEqual(turmite.x, -1)
        self.assertEqual(turmite.y, 0)

    def test_move_right(self):
        """
        Tests moving the turmite right.
        """
        turmite = Turmite()
        turmite.dir = "r"
        turmite.move()
        self.assertEqual(turmite.x, 1)
        self.assertEqual(turmite.y, 0)

    def test_init_grid(self):
        """
        Test grid initialisation
        """
        turmite = Turmite()
        turmite.init_grid(canvas_size=4)
        self.assertEqual(turmite.x, 2)
        self.assertEqual(turmite.y, 2)

    def test_init_grid_no_offset(self):
        """
        Test grid initialisation without offseting turmite position
        """
        turmite = Turmite()
        turmite.init_grid(canvas_size=4, offset=False)
        self.assertEqual(turmite.x, 0)
        self.assertEqual(turmite.y, 0)


if __name__ == "__main__":
    unittest.main()
