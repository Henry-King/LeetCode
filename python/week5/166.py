import math


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ret = []
        if numerator:
            if (numerator > 0 > denominator) or (denominator > 0 > numerator):
                ret.append('-')
            numerator = int(math.fabs(numerator))
            denominator = int(math.fabs(denominator))
            quotient, remainder = divmod(numerator, denominator)
            ret.append(str(quotient))

            if remainder:
                ret.append('.')
                remainders = {}
                while remainder not in remainders:
                    remainders[remainder] = len(ret)
                    quotient, remainder = divmod(remainder * 10, denominator)
                    ret.append(str(quotient))
                index = remainders[remainder]
                ret.insert(index, '(')
                ret.append(')')
                result = "".join(ret)
                result = result.replace('(0)', '')
                return result
            else:
                return "".join(ret)
        else:
            return str(0)


s = Solution()
print s.fractionToDecimal(0, 3)
