from src.leet_code75.day3_merge_two_sorted_lists import merge_two_lists


class TestMergeTwoSortedLists:
    def test_example1(self):
        assert merge_two_lists(list1=[1, 2, 4], list2=[1, 3, 4]) == [
            1,
            1,
            2,
            3,
            4,
            4,
        ]

    def test_example2(self):
        assert merge_two_lists(list1=[], list2=[]) == []

    def test_example3(self):
        assert merge_two_lists(list1=[], list2=[0]) == [0]
