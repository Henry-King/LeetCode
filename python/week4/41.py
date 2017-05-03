class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for index in xrange(length):
            value = nums[index]
            while 0 < value <= length and value != nums[value-1]:
                nums[index], nums[value - 1] = nums[value - 1], nums[index]
                value = nums[index]

        for index, value in enumerate(nums):
            if index + 1 != value:
                return index + 1

        return length + 1


s = Solution()
print s.firstMissingPositive([1, 1])
