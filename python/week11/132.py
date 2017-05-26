class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        cut = [i for i in xrange(len(s))]
        mem = [[False for j in xrange(len(s))] for i in xrange(len(s))]
        for i in xrange(len(s)):
            for j in xrange(i + 1):
                if s[i] == s[j] and (j + 1 > i - 1 or mem[j + 1][i - 1]):
                    mem[j][i] = True
                    cut[i] = 0 if j == 0 else min(cut[i], cut[j - 1] + 1)
        return cut[len(cut) - 1]
