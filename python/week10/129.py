# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)

    def helper(self, root, sums):
        if root:
            if not root.left and not root.right:
                return sums * 10 + root.val
            else:
                return self.helper(root.left, sums * 10 + root.val) + self.helper(root.right, sums * 10 + root.val)
        else:
            return 0
