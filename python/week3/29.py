class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        sub = divisor
        ret = 0
        count = 1 if dividend >= divisor else 0

        while dividend >= divisor:
            if dividend >= sub:
                dividend -= sub
                ret += count
                sub <<= 1
                count <<= 1
            else:
                sub >>= 1
                count >>= 1

        if not positive:
            ret = -ret
        return min((2 << 30) - 1, max(ret, -2 << 30))


s = Solution()
print s.divide(-2147483648, -1)
