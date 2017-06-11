# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        def replace(pre, cur):
            pre.val = cur.val
            if cur.next:
                replace(cur, cur.next)
            else:
                pre.next = None

        replace(node, node.next)
