class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        value_to_index = {}
        for index, value in enumerate(nums):
            search = target - value
            if search in value_to_index:
                return [value_to_index[search], index]
            else:
                value_to_index[value] = index


p = Solution()
print p.twoSum([3, 2, 4], 6)
