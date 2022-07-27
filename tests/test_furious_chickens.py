import unittest

from src.furious_chickens import furious_chicken


class TestFuriousChickens(unittest.TestCase):
    def test___SE___test_1(self):
        self.assertEqual(furious_chicken(40, 60, 4.5), (90, 57))

    def test___SE___test_2(self):
        self.assertEqual(furious_chicken(20, 45, 2), (28, 9))
