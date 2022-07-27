import unittest

from src.central_tendency import Stat


class TestCentralTendency(unittest.TestCase):
    def test___CS___mean_A(self):
        stat = Stat([13, 18, 13, 14, 13, 16, 14, 21, 13])
        self.assertEqual(stat.mean(), 15, 0)

    def test___CS___mean_B(self):
        stat = Stat([2, 7, 1, 4])
        self.assertAlmostEqual(stat.mean(), 3.5, 0)

    def test___CS___mean_C(self):
        stat = Stat([10, 13, 12, 11, 11, 10, 10, 9, 11, 8])
        self.assertEqual(stat.mean(), 10.5, 0)

    def test___SL___median_A(self):
        stat = Stat([13, 18, 13, 14, 13, 16, 14, 21, 13])
        self.assertEqual(stat.median(), 14)

    def test___SL___median_B(self):
        stat = Stat([2, 7, 1, 4])
        self.assertEqual(stat.median(), 3)

    def test___SL___median_C(self):
        stat = Stat([10, 13, 12, 11, 11, 10, 10, 9, 11, 8])
        self.assertEqual(stat.median(), 10.5)

    def test___DS___mode_A(self):
        stat = Stat([13, 18, 13, 14, 13, 16, 14, 21, 13])
        self.assertEqual(stat.mode(), [13])

    def test___DS___mode_B(self):
        stat = Stat([2, 7, 1, 4])
        self.assertEqual(stat.mode(), [])

    def test___DS___mode_C(self):
        stat = Stat([10, 13, 12, 11, 11, 10, 10, 9, 11, 8])
        self.assertEqual(stat.mode(), [10, 11])

    def test___SL___range_A(self):
        stat = Stat([13, 18, 13, 14, 13, 16, 14, 21, 13])
        self.assertEqual(stat.range(), 8)

    def test___SL___range_B(self):
        stat = Stat([2, 7, 1, 4])
        self.assertEqual(stat.range(), 6)

    def test___SL___range_C(self):
        stat = Stat([10, 13, 12, 11, 11, 10, 10, 9, 11, 8])
        self.assertEqual(stat.range(), 5)
