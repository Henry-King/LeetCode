# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        right = dummy
        left = dummy
        for i in range(n):
            right = right.next
        while right.next is not None:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None