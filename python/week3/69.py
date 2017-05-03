class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        pre_value = x / 2.0

        while pre_value:
            next_value = 0.5 * (x / pre_value + pre_value)
            if next_value == pre_value:
                return int(pre_value)
            else:
                pre_value = next_value

        return 0


s = Solution()
print s.mySqrt(0)
