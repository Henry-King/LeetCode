class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_index = 0
        value = None

        for search_index in xrange(len(nums)):
            if nums[search_index] != value:
                value = nums[search_index]
                nums[search_index], nums[unique_index] = nums[unique_index], nums[search_index]
                unique_index += 1

        return unique_index


s = Solution()
x = [1, 1, 2]
print s.removeDuplicates(x)
print x
