
"""
Given a singly linked list, determine if it is a palindrome.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        store = []
        while head != None:
            store.append(head.val)
            head = head.next

        reversed_store = store[::-1]
        return store == reversed_store
