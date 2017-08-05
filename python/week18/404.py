# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ret = 0

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def work(node):
            if node:
                if node.left:
                    if not node.left.left and not node.left.right:
                        self.ret += node.left.val
                    else:
                        work(node.left)
                work(node.right)

        work(root)
        return self.ret
