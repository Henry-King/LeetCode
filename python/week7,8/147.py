# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur_node = head
        nil = ListNode(None)
        pre_node = None
        while cur_node:
            next_node = cur_node.next

            # Reset pre_noe only when it is necessary
            if pre_node is None or pre_node.val > cur_node.val:
                pre_node = nil
            while pre_node.next and pre_node.next.val < cur_node.val:
                pre_node = pre_node.next

            cur_node.next = pre_node.next
            pre_node.next = cur_node
            cur_node = next_node
        return nil.next


a = ListNode(3)
b = ListNode(4)
c = ListNode(1)
d = ListNode(3)
e = ListNode(4)
f = ListNode(5)
g = ListNode(6)
a.next = b
b.next = c
# c.next = d
# d.next = e
# e.next = f
# f.next = g

s = Solution()
r = s.insertionSortList(a)
print r
