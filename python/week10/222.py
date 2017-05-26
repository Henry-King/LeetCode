# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def height(node):
            if node:
                return 1 + height(node.left)
            else:
                return 0

        tree_height = height(root)
        if tree_height == 0:
            return tree_height
        else:
            if height(root.right) == tree_height - 1:
                return (1 << tree_height - 1) + self.countNodes(root.right)
            else:
                return (1 << tree_height - 2) + self.countNodes(root.left)
