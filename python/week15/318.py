class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        word_set = []
        for word in words:
            word_set.append((len(word), set(word)))

        maximum = 0
        for i in xrange(len(word_set)):
            for j in xrange(i + 1, len(word_set)):
                if word_set[i][1].isdisjoint(word_set[j][1]):
                    maximum = max(maximum, word_set[i][0] * word_set[j][0])
        return maximum


s = Solution()
print s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
