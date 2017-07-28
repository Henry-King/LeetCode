from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = -1
        letter_counter = Counter(s)
        for index, letter in enumerate(s):
            if letter_counter[letter] == 1:
                ret = index
                break
        return ret


s = Solution()
print s.firstUniqChar("loveleetcode")
