# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        original_head = head
        pre_node = None
        need_reverse = False

        for i in xrange(k):
            if not head:
                need_reverse = True
                break
            else:
                head, pre_node = self.__process(head, pre_node)

        if need_reverse:
            while head != original_head:
                pre_node, head = self.__process(pre_node, head)
            ret = head
        else:
            original_head.next = self.reverseKGroup(head, k)
            ret = pre_node
        return ret

    def __process(self, head, pre_node):
        next_node = head.next
        head.next = pre_node
        pre_node = head
        head = next_node
        return head, pre_node


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


s = Solution()
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)

result = s.reverseKGroup(a, 3)
while result:
    print result.val
    result = result.next
