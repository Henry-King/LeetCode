class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        prefix_function = self.__build_prefix_function(needle)
        m = len(needle)
        q = 0
        if needle:
            for index, char in enumerate(haystack):
                while q > 0 and needle[q] != char:
                    q = prefix_function[q-1]
                if char == needle[q]:
                    q += 1
                if q == m:
                    return index-m+1
            return -1
        else:
            return 0

    def __build_prefix_function(self, pattern):
        prefix_func = []
        if pattern:
            q = 0
            prefix_func.append(q)
            for index, char in enumerate(pattern[1:], 1):
                while q > 0 and char != pattern[q]:
                    q = prefix_func[q-1]
                if char == pattern[q]:
                    q += 1
                prefix_func.append(q)
        return prefix_func


s = Solution()
print s.strStr("bbaa","aab")
