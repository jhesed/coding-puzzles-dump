import unittest

from src.patterns import count_patterns_from


class TestPatterns(unittest.TestCase):
    def test___DS___case_1(self):
        self.assertEqual(count_patterns_from("A", 10), 0)

    def test___DS___case_2(self):
        self.assertEqual(count_patterns_from("A", 0), 0)
