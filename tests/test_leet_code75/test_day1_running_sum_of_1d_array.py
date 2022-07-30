from src.leet_code75.day1_running_sum_of_1d_array import compute_running_sum


class TestDay1RunningSumOf1dArray:
    def test_running_sum1(self):
        assert compute_running_sum(nums=[1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]

    def test_running_sum2(self):
        assert compute_running_sum(nums=[3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
