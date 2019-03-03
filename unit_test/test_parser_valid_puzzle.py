import unittest

from src import parser
from src import config


class TestParserWrongPuzzle(unittest.TestCase):

    def test_simple_3x3(self):
        valid_grid = [1, 7, 0, 8, 5, 3, 6, 4, 2]
        get = parser.parser("unit_test/valid_puzzle/simple_3x3.txt")
        self.assertEqual(get, valid_grid)
        self.assertEqual(config.TAQUIN_SIZE, 3)

    def test_simple_4x4(self):
        valid_grid = [14, 6, 9, 5, 4, 12, 3, 11, 10, 15, 13, 0, 1, 8, 2, 7]
        get = parser.parser("unit_test/valid_puzzle/simple_4x4.txt")
        self.assertEqual(get, valid_grid)
        self.assertEqual(config.TAQUIN_SIZE, 4)

    def test_simple_2x2(self):
        valid_grid = [1, 0, 3, 2]
        get = parser.parser("unit_test/valid_puzzle/simple_2x2.txt")
        self.assertEqual(get, valid_grid)
        self.assertEqual(config.TAQUIN_SIZE, 2)

    def test_complex_file_1(self):
        valid_grid = [2, 3, 1, 0, 4, 5, 6, 7, 8]
        get = parser.parser("unit_test/valid_puzzle/complex_file_1.txt")
        self.assertEqual(get, valid_grid)
        self.assertEqual(config.TAQUIN_SIZE, 3)

