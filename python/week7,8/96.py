class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = [0] * (n + 1)
        ret[0] = ret[1] = 1
        for i in xrange(2, n + 1):
            for j in xrange(1, i + 1):
                ret[i] += ret[j - 1] * ret[i - j]

        return ret.pop()


s = Solution()
print s.numTrees(3)
