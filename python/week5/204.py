import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        flags = [True if i > 1 else False for i in range(0, n)]
        for i in xrange(2, int(math.sqrt(n)) + 1):
            if flags[i]:
                for j in xrange(i * i, n, i):
                    flags[j] = False
        return flags.count(True)


s = Solution()
print s.countPrimes(8)
