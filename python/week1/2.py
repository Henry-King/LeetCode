# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            val1, val2 = 0, 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            carry, remainder = divmod(val1 + val2 + carry, 10)
            n.next = ListNode(remainder)
            n = n.next
        return root.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


s = Solution()

l11 = ListNode(3)
l11.next = ListNode(7)

l22 = ListNode(9)
l22.next = ListNode(2)

print s.addTwoNumbers(l11, l22).val
