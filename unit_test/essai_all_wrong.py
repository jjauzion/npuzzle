import unittest
from pathlib import Path

from src import parser


class TestParserWrongPuzzle(unittest.TestCase):

    def test_all(self):
        puzzle_list = [file for file in Path("unit_test/wrong_puzzle").iterdir() if file.suffix == ".txt"]
        for puzzle in puzzle_list:
            print("testing '{}'".format(puzzle))
            with self.assertRaises(SystemExit) as cm:
                parser.parser(str(puzzle))
            self.assertEqual(cm.exception.code, 1)
            print(".", end="")
