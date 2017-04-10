import itertools


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return list(itertools.combinations(xrange(1, n + 1), k))


s = Solution()
print s.combine(4, 3)
