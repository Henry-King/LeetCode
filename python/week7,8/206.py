# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            new_head, new_tail = self.helper(head)
            return new_head
        else:
            return None

    def helper(self, head):
        if head.next:
            new_head, tail = self.helper(head.next)
            tail.next = head
            head.next = None
            return new_head, head
        else:
            return head, head


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
# b.next = c
# c.next = d
# d.next = e

s = Solution()
ret = s.helper(a)
print ret
