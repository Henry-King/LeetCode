# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                head = self.deleteDuplicates(head.next)
            else:
                head.next = self.deleteDuplicates(head.next)
            return head
        else:
            return None


a = ListNode(1)
b = ListNode(1)
c = ListNode(2)

d = ListNode(1)
e = ListNode(1)
f = ListNode(1)
g = ListNode(2)
h = ListNode(3)
i = ListNode(4)
j = ListNode(5)

a.next = b
b.next = c

d.next = e
e.next = f
f.next = g
g.next = h
# h.next = i
# i.next = j

s = Solution()
r = s.deleteDuplicates(d)
print r
