import string


class Solution(object):
    digit_to_letter = {
        1: (),
        2: ('a', 'b', 'c'),
        3: ('d', 'e', 'f'),
        4: ('g', 'h', 'i'),
        5: ('j', 'k', 'l'),
        6: ('m', 'n', 'o'),
        7: ('p', 'q', 'r', 's'),
        8: ('t', 'u', 'v'),
        9: ('w', 'x', 'y', 'z')
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        list_digits = list(digits)
        if len(list_digits) == 0:
            return []
        else:
            begin = [x for x in Solution.digit_to_letter[string.atoi(list_digits[0])]]
            if len(list_digits) == 1:
                ret = begin
            else:
                del list_digits[0]
                ret = reduce(lambda foo, bar: [x + y for x in foo for y in Solution.digit_to_letter[string.atoi(bar)]],
                             list_digits, begin)
            return ret


s = Solution()
print s.letterCombinations("2")
