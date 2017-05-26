class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        flags = [True if i == 0 else False for i in xrange(len(s) + 1)]
        for end in xrange(1, len(s) + 1):
            for start in xrange(0, end):
                if flags[start] and s[start:end] in wordDict:
                    flags[end] = True
                    break
        return flags[-1]


s = Solution()
print s.wordBreak("leetcode", ["leet", "code"])
