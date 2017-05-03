class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        self.pair_num = n
        self.__findCatalan(0, 0, "", ret)
        return ret

    def __findCatalan(self, left_num, right_num, cur, ret):
        if len(cur) == self.pair_num * 2:
            ret.append(cur)
        else:
            if left_num < self.pair_num:
                self.__findCatalan(left_num + 1, right_num, cur + "(", ret)
            if right_num < left_num:
                self.__findCatalan(left_num, right_num + 1, cur + ")", ret)


s = Solution()
print s.generateParenthesis(3)
