class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        else:
            ret = [0] * (len(s) + 1)
            ret[0] = 1
            ret[1] = 0 if s[0] == '0' else 1
            for index in xrange(2, len(s) + 1):
                one_digit = int(s[index - 1:index])
                two_digit = int(s[index - 2:index])
                if one_digit > 0:
                    ret[index] += ret[index - 1]
                if 10 <= two_digit <= 26:
                    ret[index] += ret[index-2]
            return ret.pop()


s = Solution()
print s.numDecodings('100')
