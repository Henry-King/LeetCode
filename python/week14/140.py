class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        sentence_from_index = {len(s): ['']}

        def sentence(i):
            if i not in sentence_from_index:
                sentence_from_index[i] = [s[i:j] + (suffix and ' ' + suffix) for j in xrange(i + 1, len(s) + 1) if
                                          s[i:j] in wordDict for suffix in sentence(j)]
            return sentence_from_index[i]

        return sentence(0)


s = Solution()
print s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
