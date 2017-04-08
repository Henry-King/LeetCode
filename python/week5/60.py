class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        options = [i for i in xrange(1, n + 1)]
        ret = []
        factorials = [1]
        for i in xrange(1, n - 1):
            factorials.append(factorials[i - 1] * (i + 1))
        place = k - 1

        for i in xrange(len(factorials) - 1, -1, -1):
            index, place = divmod(place, factorials[i])
            ret.append(str(options[index]))
            del options[index]

        if options:
            ret.append(str(options[0]))
        return "".join(ret)


s = Solution()
print s.getPermutation(1, 1)
