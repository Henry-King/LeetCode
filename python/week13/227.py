class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s:
            num, sign, stack = 0, '+', []
            for k, v in enumerate(s):
                if v.isdigit():
                    num = num * 10 + ord(v) - ord('0')

                if not v.isspace() and not v.isdigit() or k == len(s) - 1:
                    if sign == '+':
                        stack.append(+num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(int(stack.pop() * num))
                    elif sign == '/':
                        if stack[-1] < 0 and stack[-1] % num:
                            stack.append(int(stack.pop() / num + 1))
                        else:
                            stack.append(int(stack.pop() / num))

                    sign = v
                    num = 0
            return sum(stack)
        else:
            return 0


s = Solution()
print s.calculate("10000-1000/10+100*1")
