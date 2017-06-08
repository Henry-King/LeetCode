class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones, m = 0, 1
        while m <= n:
            ones += (n / m + 8) / 10 * m + (n % m + 1 if n / m % 10 == 1 else 0)
            m *= 10
        return ones


s = Solution()
print s.countDigitOne(13)
