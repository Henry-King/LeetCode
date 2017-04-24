class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if nums is not None:
            nums.sort()
            self.__helper(nums, 0, [], ret)
        return ret

    def __helper(self, nums, index, sets, result):
        result.append(sets[:])

        for i in xrange(index, len(nums)):
            if i == index or nums[i] != nums[i - 1]:
                sets.append(nums[i])
                self.__helper(nums, i + 1, sets, result)
                sets.pop()


s = Solution()
print s.subsetsWithDup([1, 2, 2])
