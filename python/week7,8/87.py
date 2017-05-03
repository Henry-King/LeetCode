from collections import Counter


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        else:
            c1 = Counter(s1)
            c2 = Counter(s2)

            if len(c1) != len(c2):
                return False
            else:
                for k, v in c1.items():
                    if c2[k] != v:
                        return False

                for i in xrange(1, len(s1)):
                    if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                        return True
                    elif self.isScramble(s1[:i], s2[len(s2) - i:]) and self.isScramble(s1[i:], s2[:len(s2) - i]):
                        return True
                return False


s = Solution()
print s.isScramble('abb', "bab")
