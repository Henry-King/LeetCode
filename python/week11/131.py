class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ret = []
        if s:
            self.__helper(s, [], ret)
        return ret

    def __helper(self, s, cur, ret):
        if s:
            for end in xrange(len(s)):
                substring = s[:end]
                if substring == '':
                    if self.__isPalindrome(s):
                        cur.append(s)
                        ret.append(cur[:])
                        cur.pop()
                elif self.__isPalindrome(substring):
                    cur.append(substring)
                    self.__helper(s[end:], cur, ret)
                    cur.pop()
        else:
            ret.append(cur[:])

    def __isPalindrome(self, s):
        for i in xrange(len(s) / 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True


s = Solution()
print s.partition("aab")
