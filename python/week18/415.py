class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num2) > len(num1):
            num1, num2 = num2, num1

        num1, num2 = num1[::-1], num2[::-1]
        ret = []
        carry = 0

        for i in xrange(len(num1)):
            digits, carry = carry, 0
            if i < len(num2):
                digits += int(num2[i])
            digits += int(num1[i])

            if digits >= 10:
                carry = 1
                digits -= 10

            ret.append(str(digits))

        if carry:
            ret.append('1')

        ret.reverse()
        return "".join(ret)


s = Solution()
print s.addStrings('10', '43')
