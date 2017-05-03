# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root:
            ret.extend(self.inorderTraversal(root.left))
            ret.append(root.val)
            ret.extend(self.inorderTraversal(root.right))
        return ret
