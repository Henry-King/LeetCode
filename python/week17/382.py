# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.linked_list = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        head = self.linked_list
        ret, i = head.val, 1
        while head.next:
            head = head.next
            if random.randint(0, i) == i - 1:
                ret = head.val
            i += 1
        return ret


        # Your Solution object will be instantiated and called as such:
        # obj = Solution(head)
        # param_1 = obj.getRandom()
