import unittest

from src.algorithm_1.binary_search import (
    binary_search_recursive,
    binary_search_iterative,
)


class TestBinarySearch(unittest.TestCase):
    nums = [-1, 0, 3, 5, 9, 12]

    def test_example_1(self):

        assert (
            binary_search_recursive(
                nums=self.nums, target=9, low=0, high=len(self.nums)
            )
            == 4
        )

    def test_example_2(self):
        assert (
            binary_search_recursive(
                nums=self.nums, target=2, low=0, high=len(self.nums)
            )
            == -1
        )

    def test_example_3(self):
        assert binary_search_iterative(nums=self.nums, target=9) == 4

    def test_example_4(self):
        assert binary_search_iterative(nums=self.nums, target=2) == -1
