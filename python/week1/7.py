class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        answer = 0
        sign = -1 if x < 0 else 1
        while x:
            temp = answer * 10 + (abs(x) % 10 * sign)
            if temp >= 2 ** 31 - 1 or temp <= -2 ** 31:
                return 0
            answer = temp

            x = abs(x) / 10 * sign
        return answer


s = Solution()
print s.reverse(-123)
