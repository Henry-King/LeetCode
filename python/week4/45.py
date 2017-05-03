class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jump, max_reach, cur_end = 0, 0, 0
        length = len(nums)
        for index in range(length - 1):
            max_reach = max(max_reach, index + nums[index])
            if max_reach >= length - 1:
                return jump + 1
            elif cur_end == index:
                cur_end = max_reach
                jump += 1
        return jump


s = Solution()
print s.jump([2, 3, 1, 1, 4])
