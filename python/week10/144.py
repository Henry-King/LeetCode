# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def helper(node, ret):
            if node:
                ret.append(node.val)
                helper(node.left, ret)
                helper(node.right, ret)

        r = []
        helper(root, r)
        return r
