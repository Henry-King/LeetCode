# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def __init__(self):
        self.cloned = {}

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head:
            if head in self.cloned:
                return self.cloned[head]
            else:
                new_head = RandomListNode(head.label)
                self.cloned[head] = new_head
                new_head.next = self.copyRandomList(head.next)
                new_head.random = self.copyRandomList(head.random)
                return new_head
        else:
            return None
