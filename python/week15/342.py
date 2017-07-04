import math


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return math.log(num, 4) % 1 == 0 if num > 0 else False

s = Solution()
print s.isPowerOfFour(16)
