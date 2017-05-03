class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sums = 0
        j = i = 0
        total = sum(nums)
        mins = total + 1
        while j < len(nums):
            sums += nums[j]
            j += 1
            while sums >= s:
                mins = min(mins, j - i)
                sums -= nums[i]
                i += 1
        return 0 if mins == total + 1 else mins


s = Solution()
print s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
