import operator


class Solution(object):
    func_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    def __init__(self):
        self.cache = {}

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return self.__compute(input, 0, len(input))

    def __compute(self, input, start, end):
        cur_input = input[start:end]
        if cur_input.isdigit():
            return [int(cur_input)]
        else:
            ret = []
            for index in xrange(start, end):
                if input[index] in "+-*":
                    if (start, index) in self.cache:
                        before = self.cache[(start, index)]
                    else:
                        before = self.__compute(input, start, index)
                        self.cache[(start, index)] = before
                    if (index + 1, end) in self.cache:
                        after = self.cache[(index + 1, end)]
                    else:
                        after = self.__compute(input, index + 1, end)
                        self.cache[index + 1, end] = after

                    temp = [Solution.func_map[input[index]](i, j) for i in before for j in after]
                    ret.extend(temp)
            return ret


s = Solution()
print s.diffWaysToCompute("2-1-1")
