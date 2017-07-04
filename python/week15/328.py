# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd_head = odd = ListNode(None)
        even_head = even = ListNode(None)
        is_odd = True
        while head:
            if is_odd:
                odd_head.next = head
                odd_head = odd_head.next
            else:
                even_head.next = head
                even_head = even_head.next
            is_odd = not is_odd
            head = head.next

        even_head.next = None
        odd_head.next = even.next
        return odd.next

f