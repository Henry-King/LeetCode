from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        times = 0
        one = False
        for v in counter.values():
            times += v / 2 * 2
            if not one and v % 2 == 1:
                times += 1
                one = True
        return times


s = Solution()
print s.longestPalindrome("abccccdd")
