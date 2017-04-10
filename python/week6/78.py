class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        count = 1 << length
        ret = []
        for i in xrange(count):
            ret.append([nums[j] for j in xrange(length) if (1 << j) & i])
        return ret


s = Solution()
print s.subsets([1, 2, 3])
