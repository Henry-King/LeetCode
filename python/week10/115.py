class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        mem = [[1 if i == 0 else 0 for j in xrange(len(s) + 1)] for i in xrange(len(t) + 1)]

        for i in xrange(len(t)):
            for j in xrange(len(s)):
                if t[i] == s[j]:
                    mem[i + 1][j + 1] = mem[i][j] + mem[i + 1][j]
                else:
                    mem[i + 1][j + 1] = mem[i + 1][j]

        return mem[len(t)][len(s)]


s = Solution()
print s.numDistinct("rabbbit", "rabbit")
