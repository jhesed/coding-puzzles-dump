from src.leet_code75.day1_pivot_index import get_pivot_index


class TestPivotIndex:
    def test_pivot1(self):
        assert get_pivot_index(nums=[1, 7, 3, 6, 5, 6]) == 3

    def test_pivot2(self):
        assert get_pivot_index(nums=[1, 2, 3]) == -1

    def test_pivot3(self):
        assert get_pivot_index(nums=[2, 1, -1]) == 0
