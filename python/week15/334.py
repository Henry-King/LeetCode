class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c1 = c2 = None
        for num in nums:
            if c1 is None or num <= c1:
                c1 = num
            elif c2 is None or num <= c2:
                c2 = num
            else:
                return True
        return False


s = Solution()
print s.increasingTriplet([1, 2, 3, 4, 5])
