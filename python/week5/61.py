# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head and k:
            nil = ListNode(None)
            nil.next = head
            left = right = nil
            length = 0

            while right.next:
                right = right.next
                length += 1

            for i in xrange(length - k % length):
                left = left.next

            right.next = head
            new_head = left.next
            left.next = None
            return new_head
        else:
            return head


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
s = Solution()
ret = s.rotateRight(a, 99)
print ret
