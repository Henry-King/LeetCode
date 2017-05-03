class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = ""
        cur = ""
        if len(strs) > 0:
            min_len = min(map(len, strs))
            for i in range(min_len):
                cur = strs[0][0:i+1]
                count = filter(None, map(lambda x: x.startswith(cur), strs))
                if len(count) == len(strs):
                    prefix = cur
                else:
                    break
        return prefix

s = Solution()
print s.longestCommonPrefix(["hillo", 'hi'])
