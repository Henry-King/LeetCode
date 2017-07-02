class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = {}
        for word in words:
            mask = 0
            for c in set(word):
                mask |= (1 << (ord(c) - 97))
            res[mask] = max(len(word), res.get(mask, 0))

        return max([res[x] * res[y] for x in res for y in res if not x & y] or [0])


s = Solution()
print s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
