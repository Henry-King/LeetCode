from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ret = True
        letter_counter = Counter(magazine)
        for letter in ransomNote:
            if letter in letter_counter and letter_counter[letter] > 0:
                letter_counter[letter] -= 1
            else:
                ret = False
                break
        return ret


s = Solution()
print s.canConstruct("aa", "aab")
