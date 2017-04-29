# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        nil = ListNode(None)
        nil.next = head
        pre = nil
        while head:
            if val != head.val:
                pre.next = head
                pre = head
            head = head.next

        pre.next = None
        return nil.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(6)
d = ListNode(3)
e = ListNode(4)
f = ListNode(5)
g = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
s = Solution()
r = s.removeElements(a, 6)
print r
