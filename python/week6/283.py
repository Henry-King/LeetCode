class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        valid_index = 0
        for moved_index, value in enumerate(nums):
            if value:
                nums[valid_index], nums[moved_index] = nums[moved_index], nums[valid_index]
                valid_index += 1


s = Solution()
source = [0, 1, 0, 3, 12]
s.moveZeroes(source)
print source
