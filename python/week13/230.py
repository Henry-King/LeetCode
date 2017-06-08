# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        nums = []

        def travel(node):
            if node:
                travel(node.left)
                nums.append(node.val)
                travel(node.right)

        travel(root)
        return nums[k - 1]
