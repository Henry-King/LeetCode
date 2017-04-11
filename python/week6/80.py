class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        twice_index = 0
        pre_value = pre_pre_value = None

        for i, cur_value in enumerate(nums):
            if cur_value != pre_value or cur_value != pre_pre_value:
                pre_pre_value = pre_value
                pre_value = cur_value
                nums[twice_index], nums[i] = nums[i], nums[twice_index]
                twice_index += 1

        return twice_index


s = Solution()
a = [1, 1, 1, 2, 2, 3]
print s.removeDuplicates(a)
print a
