class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def is_valid(candidate):
            count = 0
            for item in candidate:
                if item == '(':
                    count += 1
                elif item == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        level = {s}
        while True:
            valid = filter(is_valid, level)
            if valid:
                return valid
            else:
                level = {s[:i] + s[i + 1:] for s in level for i in xrange(len(s))}


s = Solution()
print s.removeInvalidParentheses("(()(")
