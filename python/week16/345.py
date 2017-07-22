class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        def isVowel(letter):
            return letter in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        if s:
            head = 0
            tail = len(s) - 1
            s_list = list(s)
            while tail > head:
                if isVowel(s_list[tail]) and isVowel(s_list[head]):
                    s_list[tail], s_list[head] = s_list[head], s_list[tail]
                    tail -= 1
                    head += 1
                elif isVowel(s_list[tail]) and not isVowel(s_list[head]):
                    head += 1
                elif not isVowel(s_list[tail]) and isVowel(s_list[head]):
                    tail -= 1
                else:
                    tail -= 1
                    head += 1
            return "".join(s_list)
        else:
            return s


s = Solution()
print s.reverseVowels("aA")
