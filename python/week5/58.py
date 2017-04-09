class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        i = len(s) - 1

        for i in xrange(len(s) - 1, -1, -1):
            if not s[i].isspace():
                break

        for j in xrange(i, -1, -1):
            if s[j].isspace():
                break
            else:
                length += 1
        return length


s = Solution()
print s.lengthOfLastWord(" ")
