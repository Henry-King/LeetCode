class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        size = 0
        for num in nums:
            lo, hi = 0, size - 1
            while lo <= hi:
                mid = (lo + hi) >> 1
                if num > dp[mid]:
                    lo = mid + 1
                elif num < dp[mid]:
                    hi = mid - 1
                else:
                    break
            dp[lo] = num
            if lo == size:
                size += 1
        return size


s = Solution()
print s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
