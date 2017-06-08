class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        k2, k3, k5 = 0, 0, 0
        for i in xrange(1, n):
            res.append(min(res[k2] * 2, res[k3] * 3, res[k5] * 5))
            if res[k2] * 2 == res[i]:
                k2 += 1
            if res[k3] * 3 == res[i]:
                k3 += 1
            if res[k5] * 5 == res[i]:
                k5 += 1
        return res[-1]


s = Solution()
print s.nthUglyNumber(10)
