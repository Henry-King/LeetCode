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
                    lo = mid
                    break
            dp[lo] = num
            if lo == size:
                size += 1
        return size


s = Solution()
print s.lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12])
