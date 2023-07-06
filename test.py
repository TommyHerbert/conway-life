import four_cell_lifespans, search
import unittest

class TestFourCellLifespans(unittest.TestCase):
    def test_count_patterns(self):
        pattern_count = len(list(four_cell_lifespans.get_patterns(2, 2, 2)))
        self.assertEqual(6, pattern_count)

    def test_emptiness(self):
        empty = ((0,0,0), (0,0,0), (0,0,0))
        self.assertTrue(four_cell_lifespans.empty_pattern(empty))
        dot = ((0,0,0), (0,1,0), (0,0,0))
        self.assertFalse(four_cell_lifespans.empty_pattern(dot))

    def test_spiral(self):
        position = search.spiral(15, -4)
        self.assertEqual((15, -4), next(position))
        self.assertEqual((15, -5), next(position))
        for _ in range(8):
            next(position)
        self.assertEqual((15, -6), next(position))

if __name__ == '__main__':
    unittest.main()
