class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]
        for i in xrange(1, len(nums)):
            res.append(res[i - 1] * nums[i - 1])

        right = 1
        for i in reversed(range(len(nums))):
            res[i] *= right
            right *= nums[i]
        return res


s = Solution()
print s.productExceptSelf([1, 2, 3, 4])
