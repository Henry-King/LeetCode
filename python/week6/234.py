# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reverse = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next

        if fast:
            slow = slow.next

        while slow and slow.val == reverse.val:
            reverse = reverse.next
            slow = slow.next
        return not reverse


a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(1)

a.next = b
b.next = c
c.next = d

s = Solution()
print s.isPalindrome(a)
