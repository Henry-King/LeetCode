# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.max_value = 0

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.max_value = root.val
            self.max_path_down(root)
            return self.max_value
        else:
            return 0

    def max_path_down(self, node):
        if node:
            left = max(0, self.max_path_down(node.left))
            right = max(0, self.max_path_down(node.right))
            self.max_value = max(self.max_value, node.val + left + right)
            return max(left, right) + node.val
        else:
            return 0


a = TreeNode(1)
a.left = TreeNode(-2)
a.right = TreeNode(3)
s = Solution()
print s.maxPathSum(a)
