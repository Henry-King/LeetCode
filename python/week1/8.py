class Solution(object):
    str2int ={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

    def __init__(self):
        self.endReduce = False

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()

        if 0 == len(str):
            return 0
        else:
            if str[0] == '+':
                symbol = 1
                str = str[1:]
            elif str[0] == '-':
                symbol = -1
                str = str[1:]
            elif not str[0].isdigit():
                return 0
            else:
                symbol = 1


            digits = list(str)
            if len(digits) == 0:
                return 0
            elif len(digits) == 1:
                if digits[0] not in Solution.str2int:
                    return 0
                else:
                    return symbol*Solution.str2int[digits[0]]
            else:
                ret = reduce(self.__letter2num, digits)
                if symbol == 1:
                    if ret <= 2 ** 31 - 1:
                        pass
                    else:
                        ret = 2 ** 31 - 1
                elif symbol == -1:
                    if ret <= 2 ** 31:
                        ret *= -1
                    else:
                        ret = -2 ** 31
                else:
                    ret = 0
                return ret

    def __letter2num(self, x, y):
        if type(x) is not long and type(x) is not int and x not in Solution.str2int:
            self.endReduce = True
            return 0
        else:
            if y not in Solution.str2int:
                self.endReduce = True
                if type(x) is int:
                    return x
                elif x not in Solution.str2int:
                    return 0
                else:
                    return Solution.str2int[x]
            else:
                if type(x) is int:
                    if self.endReduce:
                        return x
                    else:
                        return x*10+Solution.str2int[y]
                elif x not in Solution.str2int:
                    return 0
                else:
                    if self.endReduce:
                        return Solution.str2int[x]
                    else:
                        return Solution.str2int[x]*10+Solution.str2int[y]

s = Solution()
print s.myAtoi("1234567890123456789012345678901234567890")