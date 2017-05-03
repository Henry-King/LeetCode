class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_value = 0
        left = -1
        stack = []
        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        max_value = max(max_value, index - stack[len(stack) - 1])
                    else:
                        max_value = max(max_value, index - left)
                else:
                    left = index
        return max_value

s = Solution()
print s.longestValidParentheses(")()())")
