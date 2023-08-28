"""
https://leetcode.com/problems/first-bad-version/
solved in leetcode env to use linked list class
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            tmp_next = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_next

        return prev
