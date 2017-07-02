class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res = [1]
        candidates = [0] * len(primes)
        for i in xrange(1, n):
            res.append(min([res[v] * primes[k] for k, v in enumerate(candidates)]))
            for k, v in enumerate(candidates):
                if res[i] == res[v] * primes[k]:
                    candidates[k] += 1
        return res[-1]


s = Solution()
print s.nthSuperUglyNumber(12, [2, 7, 13, 19])
