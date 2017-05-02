# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.prev = self.first = self.second = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.__helper(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def __helper(self, root):
        if root:
            self.__helper(root.left)
            if self.prev:
                if not self.first and self.prev.val > root.val:
                    self.first = self.prev
                if self.first and self.prev.val > root.val:
                    self.second = root
            self.prev = root
            self.__helper(root.right)
