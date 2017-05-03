class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        thousands = ['', 'M', 'MM', 'MMM']
        hundrends = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

        ret = ['' for i in xrange(4)]

        ret[0] = thousands[num / 1000]
        num %= 1000
        ret[1] = hundrends[num / 100]
        num %= 100
        ret[2] = tens[num / 10]
        num %= 10
        ret[3] = ones[num]
        return "".join(ret)


s = Solution()
print s.intToRoman(1954)
