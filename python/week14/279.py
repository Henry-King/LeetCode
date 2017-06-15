class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        else:
            dp = [i if i <= 1 else 0 for i in xrange(n + 1)]
            for i in xrange(2, n + 1):
                candidates = [dp[i - j * j] + 1 for j in xrange(1, int(i ** 0.5) + 1)]
                dp[i] = min(candidates)
            return dp[-1]


s = Solution()
print s.numSquares(7691)
