class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        int_max = 2 ** 31 - 1
        i = base = 0
        positive = True

        for i in xrange(0, len(str)):
            if str[i] == ' ':
                i += 1
            else:
                break

        if i < len(str):
            if str[i] == '+':
                i += 1
            elif str[i] == '-':
                positive = False
                i += 1

            while i < len(str) and ord('0') <= ord(str[i]) <= ord('9'):
                if base > int_max / 10 or (base == int_max / 10 and ord(str[i]) - ord('0') > 7):
                    if positive:
                        return int_max
                    else:
                        return -2 ** 31
                else:
                    base = 10 * base + (ord(str[i]) - ord('0'))
                i += 1

        return base if positive else -base


s = Solution()
print s.myAtoi("1234567890123456789012345678901234567890")
