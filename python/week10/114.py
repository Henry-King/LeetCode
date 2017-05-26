# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            stack = [root]
            child = TreeNode(None)
            while stack:
                child.right = stack.pop()
                child = child.right
                if child.right:
                    stack.append(child.right)
                if child.left:
                    stack.append(child.left)
                child.left = None
