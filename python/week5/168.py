class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = []
        n -= 1
        n, remainder = divmod(n, 26)
        ret.append(chr(ord("A") + remainder))
        while n > 0:
            n -= 1
            n, remainder = divmod(n, 26)
            ret.append(chr(ord("A") + remainder))
        ret.reverse()
        return "".join(ret)


s = Solution()
print s.convertToTitle(29)
