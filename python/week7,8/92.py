# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n or head is None or head.next is None:
            return head
        else:
            nil = ListNode(None)
            nil.next = head
            left = nil
            for i in xrange(m - 1):
                left = left.next

            start = left.next
            then = start.next
            for i in xrange(n - m):
                start.next = then.next
                then.next = left.next
                left.next = then
                then = start.next

            return nil.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

s = Solution()
r = s.reverseBetween(a, 2, 4)
while r:
    print r.val
    r = r.next
