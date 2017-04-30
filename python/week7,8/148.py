# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        else:
            pre = fast = slow = head
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next

            pre.next = None

            left = self.sortList(head)
            right = self.sortList(slow)

            return self.__merge(left, right)

    def __merge(self, left, right):
        cur = nil = ListNode(None)
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
                cur = cur.next
            else:
                cur.next = right
                right = right.next
                cur = cur.next
        if left:
            cur.next = left
        elif right:
            cur.next = right
        return nil.next

a = ListNode(2)
b = ListNode(1)
a.next = b

s = Solution()
r = s.sortList(a)
print r
