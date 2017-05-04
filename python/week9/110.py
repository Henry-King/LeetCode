# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def depth(node):
            if node:
                return 1 + max(depth(node.left), depth(node.right))
            else:
                return 0

        if root:
            left_depth = depth(root.left)
            right_depth = depth(root.right)
            return abs(left_depth - right_depth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return True


r = TreeNode(1)
r.right = TreeNode(2)
r.right.right = TreeNode(3)

s = Solution()
print s.isBalanced(r)
