import unittest

from src.word_to_numbers import word_to_number


class TestWordToNumbers(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(word_to_number("fourteen"), 14)

    def test_dashed_compound_numbers(self):
        self.assertEqual(word_to_number("seventy-two"), 72)

    def test_spaced_compound_numbers(self):
        self.assertEqual(word_to_number("seventy two"), 72)

    def test_huge_numbers(self):
        word = "eight thousand one hundred and three"
        self.assertEqual(word_to_number(word), 8_103)

    def test_millions(self):
        word = (
            "nine hundred ninety-nine million nine hundred ninety nine thousand "
            + "nine hundred ninety nine"
        )
        self.assertEqual(word_to_number(word), 999_999_999)

    def test_invalid_dash(self):
        word = "nine-hundred-ninety-five"
        self.assertEqual(word_to_number(word), "Input not a string")

    def test_invalid_comma(self):
        word = "1,2,3,4"
        self.assertEqual(word_to_number(word), "Input not a string")

    def test_and(self):
        word = "two hundred forty-five thousand and eight"
        self.assertEqual(word_to_number(word), 245008)
