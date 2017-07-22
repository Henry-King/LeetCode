class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n:
            res = 10
            unique_digit = 9
            ava = 9
            for __ in xrange(1, n):
                if unique_digit > 1:
                    ava *= unique_digit
                    res += ava
                    unique_digit -= 1
                else:
                    break
        else:
            res = 1
        return res


s = Solution()
print s.countNumbersWithUniqueDigits(0)
