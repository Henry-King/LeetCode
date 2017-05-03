class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n == -1:
            return 1 / x
        else:
            if n % 2 == 0:
                mul = self.myPow(x, n / 2)
                mul *= mul
            else:
                mul = self.myPow(x, (n - 1) / 2)
                mul = mul * mul * x

            return mul


s = Solution()
print s.myPow(34.00515, -3)
