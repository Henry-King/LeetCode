# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head:
            return self.__toBFS(head, None)
        else:
            return None

    def __toBFS(self, head, tail):
        if head == tail:
            return None
        else:
            fast = slow = head
            while fast != tail and fast.next != tail:
                fast = fast.next.next
                slow = slow.next
            root = TreeNode(slow.val)
            root.left = self.__toBFS(head, slow)
            root.right = self.__toBFS(slow.next, tail)
            return root
