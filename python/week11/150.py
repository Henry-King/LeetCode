import operator


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
        for token in tokens:
            if token in operators:
                bar, foo = stack.pop(), stack.pop()
                stack.append(operators[token](foo, bar))
            else:
                stack.append(int(token))
        return stack.pop()


s = Solution()
print s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
