import unittest
import pickle
from pathlib import Path
from src import parser


from src import PathFinder
from src import Node
from src import config


class TestParserWrongPuzzle(unittest.TestCase):

    def test_invalid_number(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/invalid_number.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_nothing(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/nothing.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_empty(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/empty.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_lonely_space(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/lonely_space.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_random(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/random.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_complex_commentInLine(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/complex_in_line_com.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_comment_in_between(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/comment_in_between.txt")
        self.assertEqual(cm.exception.code, 1)

