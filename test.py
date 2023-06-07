import four_cell_lifespans
import unittest

class TestFourCellLifespans(unittest.TestCase):
    def test_count_patterns(self):
        pattern_count = len(list(four_cell_lifespans.get_patterns(2, 2, 2)))
        self.assertEqual(6, pattern_count)

if __name__ == '__main__':
    unittest.main()
