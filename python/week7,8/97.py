class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2):
            return False
        else:
            flags = [[False] * (len(s2) + 1)] * (len(s1) + 1)
            for i in xrange(len(s1) + 1):
                for j in xrange(len(s2) + 1):
                    if i == 0 and j == 0:
                        flags[i][j] = True
                    elif i == 0:
                        flags[i][j] = flags[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                    elif j == 0:
                        flags[i][j] = flags[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                    else:
                        flags[i][j] = (flags[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                            flags[i][j - 1] and s2[j - 1] == s3[i + j - 1])
            return flags[len(s1)][len(s2)]


s = Solution()
print s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
