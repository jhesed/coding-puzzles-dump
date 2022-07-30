"""
21. Merge Two Sorted Lists

You are given the heads of two sorted
linked lists list1 and list2.
Merge the two lists in a one sorted list.
The list should be made by splicing together
the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def merge_two_lists(
    list1: Optional[list], list2: Optional[list]
) -> Optional[list]:
    """
    Visualization:
        * 1,2,4
        * 1,3,4

        index1 = 0 | list1[index1] = 1
        index2 = 0 | list2[index2] = 1
        Case: equal
        Actions:
            * Append both to list
                * merged_list = [1, 1]
            * Increment both indices


        index1 = 1 | list1[index1] = 2
        index2 = 1 | list2[index2] = 3
        Case: <
        Actions:
            * Append whichever is less than to list
                * merged_list = [1, 1, 2]
            * Increment only the index of whatever was greater
    """

    if not list1 and not list2:
        return []

    index1 = 0
    index2 = 0
    length_list1 = len(list1)
    length_list2 = len(list2)
    merged_list = []

    while len(merged_list) < (length_list1 + length_list2):

        if index1 >= length_list1:
            merged_list.extend(list2[index2:])
            break
        if index2 >= length_list2:
            merged_list.extend(list1[index1:])
            break

        if list1[index1] == list2[index2]:
            merged_list.append(list1[index1])
            merged_list.append(list1[index2])
            index1 += 1
            index2 += 1
        elif list1[index1] < list2[index2]:
            merged_list.append(list1[index1])
            index1 += 1
        elif list2[index2] < list1[index1]:
            merged_list.append(list2[index2])
            index2 += 1
        else:
            print("Unknown error")

    return merged_list
