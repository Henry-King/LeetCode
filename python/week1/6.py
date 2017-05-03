class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = [[] for i in xrange(numRows)]
        length = len(s)
        i = 0
        while i < length:
            for j in xrange(numRows):
                if i >= length:
                    break
                else:
                    rows[j].append(s[i])
                    i += 1
            for j in xrange(numRows - 2, 0, -1):
                if i >= length:
                    break
                else:
                    rows[j].append(s[i])
                    i += 1
        ret = reduce(lambda a, b: a+b, rows)
        return "".join(ret)


s = Solution()
print s.convert("PAYPALISHIRING", 3)
