class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1

            if count <= mid:
                lo = mid + 1
            else:
                hi = mid
        return lo


s = Solution()
print s.findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1])
