class Solution(object):
    matches = {')': '(', ']': '[', '}': '{'}

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tokens = list(s)
        stack = []
        for item in tokens:
            if item == '(' or item == '[' or item == '{':
                stack.append(item)
            else:
                match = Solution.matches[item]
                if not stack or stack.pop() != match:
                    return False
        return False if stack else True

s = Solution()
print s.isValid("]")
