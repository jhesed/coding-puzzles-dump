import unittest

from src.bigger_number2 import next_bigger


class TesttBiggerSimilarDigits(unittest.TestCase):
    def test___one(self):
        self.assertEqual(next_bigger(12), 21)

    def test___two(self):
        self.assertEqual(next_bigger(790), 907)

    def test___three(self):
        self.assertEqual(next_bigger(111), -1)
