class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n0 = n1 = n2 = 0
        for index, value in enumerate(nums):
            if value == 0:
                nums[n2], nums[n1], nums[n0] = 2, 1, 0
                n0, n1, n2 = n0 + 1, n1 + 1, n2 + 1
            elif value == 1:
                nums[n2], nums[n1] = 2, 1
                n1, n2 = n1 + 1, n2 + 1
            elif value == 2:
                nums[n2] = 2
                n2 += 1
