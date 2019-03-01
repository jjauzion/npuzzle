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

    def test_doublon(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/doublon.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_doublon_2(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/doublon_2.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_int_max(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/int_max.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_int_max_2(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/int_max_2.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_invalid_char(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/invalid_char.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_invalid_char_2(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/invalid_char_2.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_invalid_number(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/invalid_number.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_negative_number(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/negative_number.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_too_many_columns(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/too_many_columns.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_too_many_columns_2(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/too_many_columns_2.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_too_many_lines(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/too_many_lines.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_wrong_1st_line(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/wrong_1st_line.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_wrong_1st_line_2(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/wrong_1st_line_2.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_wrong_1st_line_3(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/wrong_1st_line_3.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_wrong_size(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/wrong_size.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_wrong_size_2(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/wrong_size_2.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_wrong_size_3(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/wrong_size_3.txt")
        self.assertEqual(cm.exception.code, 1)

    def test_too_many_columns_2(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parser("unit_test/wrong_puzzle/too_many_columns_2.txt")
        self.assertEqual(cm.exception.code, 1)
