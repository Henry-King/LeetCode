import collections


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            return self.multiply(num2, num1)
        else:
            num2 = list(num2)
            num1 = list(num1)
            num2.reverse()
            ret = collections.deque()
            for count, multiplier in enumerate(num2):
                mul = self.__multiply(num1, multiplier)
                mul.extend(['0'] * count)
                ret = self.__add(ret, mul)
            return "".join(ret)

    def __multiply(self, num1, num2):
        ret = collections.deque()
        multiplier = int(num2)
        if multiplier == 0:
            ret.append('0')
        elif multiplier == 1:
            ret.extend(num1)
        else:
            carry, remainder = 0, 0
            for multiplicand in reversed(num1):
                mul = multiplier * int(multiplicand)
                mul += carry
                carry, remainder = divmod(mul, 10)
                ret.appendleft(str(remainder))
            if carry:
                ret.appendleft(str(carry))
        return ret

    def __add(self, num1, num2):
        ret = collections.deque()
        carry = 0
        offset = -1

        num1_length = len(num1)
        num2_length = len(num2)
        max_length = max(num1_length, num2_length)

        while offset >= -max_length or carry:
            val1, val2 = 0, 0
            if offset >= -num1_length:
                val1 = int(num1[offset])
            if offset >= -num2_length:
                val2 = int(num2[offset])
            carry, remainder = divmod(val1 + val2 + carry, 10)
            ret.appendleft(str(remainder))
            offset -= 1
        return ret


s = Solution()
print s.multiply("123","456")
