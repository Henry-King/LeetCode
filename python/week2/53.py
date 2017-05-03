class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = nums[0]
        max_ending_here = nums[0]
        for value in nums[1:]:
            max_ending_here = max(max_ending_here + value, value)
            max_so_far = max(max_ending_here, max_so_far)
        return max_so_far


s = Solution()
print s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
