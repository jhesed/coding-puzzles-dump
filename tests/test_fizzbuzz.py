import unittest

from src.fizzbuzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_example_1(self):
        assert fizz_buzz(n=3) == ["1", "2", "Fizz"]

    def test_example_2(self):
        assert fizz_buzz(n=5) == ["1", "2", "Fizz", "4", "Buzz"]

    def test_example_3(self):
        assert fizz_buzz(n=15) == [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ]
