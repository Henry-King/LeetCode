class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s[::-1]
        for i in xrange(len(r) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s


s = Solution()
print s.shortestPalindrome("abcd")
