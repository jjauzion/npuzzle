import unittest

from src import parser
from src import error


class TestParserWrongPuzzle(unittest.TestCase):

    def test_nothing(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/nothing.txt")

    def test_empty(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/empty.txt")

    def test_lonely_space(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/lonely_space.txt")

    def test_random(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/random.txt")

    def test_complex_commentInLine(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/complex_in_line_com.txt")

    def test_comment_in_between(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/comment_in_between.txt")

    def test_doublon(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/doublon.txt")

    def test_doublon_2(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/doublon_2.txt")

    def test_int_max(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/int_max.txt")

    def test_int_max_2(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/int_max_2.txt")

    def test_invalid_char(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/invalid_char.txt")

    def test_invalid_char_2(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/invalid_char_2.txt")

    def test_invalid_number(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/invalid_number.txt")

    def test_negative_number(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/negative_number.txt")

    def test_too_many_columns(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/too_many_columns.txt")

    def test_too_many_columns_2(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/too_many_columns_2.txt")

    def test_too_many_lines(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/too_many_lines.txt")

    def test_wrong_1st_line(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/wrong_1st_line.txt")

    def test_wrong_1st_line_2(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/wrong_1st_line_2.txt")

    def test_wrong_1st_line_3(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/wrong_1st_line_3.txt")

    def test_wrong_size(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/wrong_size.txt")

    def test_wrong_size_2(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/wrong_size_2.txt")

    def test_wrong_size_3(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/wrong_size_3.txt")

    def test_1x1(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/1x1.txt")

    def test_no_zero(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/no_zero.txt")

    def test_only_zero(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/only_zero.txt")

    def test_2_zero(self):
        with self.assertRaises(error.ParsingError):
            parser.parser("unit_test/wrong_puzzle/2_zero.txt")
