# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def toBST(start, end):
            if start <= end:
                mid = (start + end) / 2
                root = TreeNode(nums[mid])
                root.left = toBST(start, mid - 1)
                root.right = toBST(mid + 1, end)
                return root
            else:
                return None

        if nums:
            return toBST(0, len(nums) - 1)
        else:
            return None

s = Solution()
s.sortedArrayToBST([1,2,3,4])
