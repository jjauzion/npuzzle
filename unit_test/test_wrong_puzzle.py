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
