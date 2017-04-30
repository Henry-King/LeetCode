# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next:
            p1 = p2 = head
            while p2.next and p2.next.next:
                p1 = p1.next
                p2 = p2.next.next

            pre_mid = p1
            pre_cur = pre_mid.next
            new_head = None
            while pre_cur:
                cur = pre_cur.next
                pre_cur.next = new_head
                new_head = pre_cur
                pre_cur = cur
            pre_mid.next = new_head

            p1 = head
            p2 = pre_mid.next
            while p1 != pre_mid:
                pre_mid.next = p2.next
                p2.next = p1.next
                p1.next = p2
                p1 = p2.next
                p2 = pre_mid.next
