from src.leet_code75.day3_merge_two_sorted_linked_list import (
    merge_two_lists,
    ListNode,
)


class TestMergeTwoSortedLists:
    def test_example1(self):
        merged_nodes = merge_two_lists(
            list1=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4))),
            list2=ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4))),
        )

        while merged_nodes.next:
            print(merged_nodes.val)
            merged_nodes = merged_nodes.next

        # TODO: Assertion

    def test_example2(self):
        assert not merge_two_lists(
            list1=ListNode(val=None), list2=ListNode(val=None)
        )

    def test_example3(self):
        assert (
            merge_two_lists(list1=ListNode(val=None), list2=ListNode())
            == ListNode()
        )
