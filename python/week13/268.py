class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for k, v in enumerate(nums):
            res ^= v ^ k
        return res ^ len(nums)


s = Solution()
print s.missingNumber([0, 1, 3])
