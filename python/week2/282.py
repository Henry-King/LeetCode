class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        else:
            rst = []
            self.__compute(num, target, rst, "", 0, 0, 0)
            return rst

    def __compute(self, num_str, target, matches, sequence_so_far, position, computed_value, multiple_value):
        if position == len(num_str):
            if target == computed_value:
                matches.append(sequence_so_far)
        else:
            for index, value in enumerate(num_str[position:], position):
                if index != position and num_str[position] == '0':
                    break
                else:
                    cur_num_str = num_str[position:index + 1]
                    cur_num = long(cur_num_str)
                    if position == 0:
                        self.__compute(num_str, target, matches, sequence_so_far + cur_num_str, index + 1, cur_num,
                                       cur_num)
                    else:
                        self.__compute(num_str, target, matches, sequence_so_far + '+' + cur_num_str, index + 1,
                                       computed_value + cur_num, cur_num)
                        self.__compute(num_str, target, matches, sequence_so_far + '-' + cur_num_str, index + 1,
                                       computed_value - cur_num, -cur_num)
                        self.__compute(num_str, target, matches, sequence_so_far + '*' + cur_num_str, index + 1,
                                       computed_value - multiple_value + multiple_value * cur_num,
                                       cur_num * multiple_value)


s = Solution()
actual = s.addOperators("123456789", 45)
