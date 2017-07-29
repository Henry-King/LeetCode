import random


class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ret = None
        count = 0
        for index, num in enumerate(self.nums):
            if num == target:
                if random.randint(0, count) == 0:
                    ret = index
                count += 1
        return ret


        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.pick(target)
