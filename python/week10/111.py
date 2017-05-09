# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            left_depth = self.minDepth(root.left)
            right_depth = self.minDepth(root.right)
            if not root.left or not root.right:
                return 1 + left_depth + right_depth
            else:
                return 1 + min(left_depth, right_depth)
        else:
            return 0
