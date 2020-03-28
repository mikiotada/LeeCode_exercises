"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""

# the solution is provided by LeeCode. 


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        if l1 is not None:
            prev.next = l1
        else:
            prev.next = l2

        return prehead.next
