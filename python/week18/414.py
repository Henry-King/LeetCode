class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second, third = None, None, None
        for num in nums:
            if not first or num > first:
                third, second, first = second, first, num
            elif num < first and (not second or num > second):
                third, second = second, num
            elif num < second and (not third or num > third):
                third = num
        return first if third is None else third


s = Solution()
print s.thirdMax([3, 2, 1])
print s.thirdMax([1, 2])
print s.thirdMax([2, 2, 3, 1])
print s.thirdMax([3, 3, 4, 3, 4, 3, 0, 3, 3])
