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


class ListNode:
    """
    This is the contract provided by the challenge.
    Hence, we won't be restructuring this.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:

    merged_list = ListNode()
    tail = merged_list

    while True:
        if not list1.val:
            tail.next = list2.next
            break
        if not list2.val:
            tail.next = list1.next
            break

    return merged_list.next


'''
def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:

    merged_list = ListNode(val=list1.val) if list1.val > list2.val else ListNode(val=list2.val)
    pointer = merged_list

    while True:
        pointer = pointer.next

        if not list1.next:
            pointer.next = list2.next
            break
        if not list2.next:
            pointer.next = list1.next
            break

        if list1.next.val < list2.next.val:
            pointer.next = list1.next
            list1 = list1.next

        elif list2.next.val < list1.next.val:
            pointer.next = list2.next
            list2 = list2.next

        elif list1.next.val == list2.next.val:

            pointer.next = list1.next
            merged_list.next = pointer

            pointer.next = list2.next

            list1 = list1.next
            list2 = list2.next

        merged_list.next = pointer

    # Add last pointer after break
    merged_list.next = pointer

    return merged_list

def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
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
        return

    node_list1 = list1
    node_list2 = list2
    
    
    if node_list1.val < node_list2.val:
        print({"src": "A", "val": node_list1.val})
        merged_nodes = node_list1
        node_list1 = node_list1.next
    else:
        print({"src": "B", "val": node_list2.val})
        merged_nodes = node_list2
        node_list2 = node_list2.next

    while True:

        if not node_list1.next:
            print({"src": "C", "val": node_list2.val})
            merged_nodes.next = node_list2
            break

        if not node_list2.next:
            print({"src": "D", "val": node_list1.val})
            merged_nodes.next = node_list1.next
            break

        if node_list1.val == node_list2.val:
            print({"src": "E", "val": node_list2.val})
            print({"src": "E", "val": node_list1.val})
            merged_nodes.next = node_list1
            merged_nodes.next.next = node_list2
            node_list1 = node_list1.next
            node_list2 = node_list2.next

        elif node_list1.val < node_list2.val:
            print({"src": "F", "val": node_list1.val})
            merged_nodes.next = node_list1
            node_list1 = node_list1.next

        elif node_list2.val < node_list1.val:
            print({"src": "G", "val": node_list2.val})
            merged_nodes.next = ListNode(val=node_list2.val)
            node_list2 = node_list2.next

    return merged_nodes

'''
