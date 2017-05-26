from collections import Counter


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        min_letter_index = 0
        for index, letter in enumerate(s):
            if ord(letter) < ord(s[min_letter_index]):
                min_letter_index = index

            times = count[letter] - 1
            if times == 0:
                break
            else:
                count[letter] = times

        return "" if s == '' else s[min_letter_index] + self.removeDuplicateLetters(
            s[min_letter_index + 1:].replace(s[min_letter_index], ""))


s = Solution()
print s.removeDuplicateLetters("cbacdcbc")
