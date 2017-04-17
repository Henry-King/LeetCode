# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left = lnil = ListNode(None)
        right = rnil = ListNode(None)
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next

        right.next = None
        left.next = rnil.next

        return lnil.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

s = Solution()
r = s.partition(a, 4)
while r:
    print r.val
    r = r.next
