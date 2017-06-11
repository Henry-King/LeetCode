class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret = []
        if len(nums) == 1:
            ret.append(str(nums[0]))
        elif len(nums) > 1:
            interval_start = nums[0]
            for k, v in enumerate(nums[1:], 1):
                previous_num = nums[k - 1]
                if v - previous_num != 1:
                    ret.append(self.___create_interval(interval_start, previous_num))
                    interval_start = v

            ret.append(self.___create_interval(interval_start, nums[-1]))
        return ret

    def ___create_interval(self, interval_start, previous_num):
        if previous_num == interval_start:
            return str(interval_start)
        else:
            return "".join([str(interval_start), "->", str(previous_num)])


s = Solution()
print s.summaryRanges([0, 1, 2, 4, 5, 7])
