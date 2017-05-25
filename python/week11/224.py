class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result, num, sign = 0, 0, 1
        for letter in s:
            if letter.isdigit():
                num = num * 10 + int(letter)
            elif letter == '+':
                result += sign * num
                num = 0
                sign = 1
            elif letter == '-':
                result += sign * num
                num = 0
                sign = -1
            elif letter == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif letter == ')':
                result += sign * num
                result *= stack.pop()
                result += stack.pop()
                num = 0
        if num != 0:
            result += sign * num
        return result


s = Solution()
print s.calculate("(1+(4+5+2)-3)+(6+8)")
