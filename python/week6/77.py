class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]
        else:
            if n - k < k:
                return [[i for i in xrange(1, n + 1) if i not in item] for item in self.combine(n, n - k)]
            else:
                return [pre + [i] for i in xrange(1, n + 1) for pre in self.combine(i - 1, k - 1)]


s = Solution()
print s.combine(3, 3)
