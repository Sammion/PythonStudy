"""

Reverse a linked list.

翻转一个链表

Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if head is None: return None
        p = head
        cur = None
        pre = None
        while p is not None:
            cur = p.next
            p.next = pre
            pre = p
            p = cur
        return pre