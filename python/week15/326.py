import math


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (math.log10(n) / math.log10(3)) % 1 == 0 if n > 0 else False


s = Solution()
print s.isPowerOfThree(4)
