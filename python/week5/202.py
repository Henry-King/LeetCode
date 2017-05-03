class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.__is_happy(n, set())

    def __is_happy(self, n, foo):
        ret = 0
        while n > 0:
            n, remainder = divmod(n, 10)
            ret += remainder * remainder

        if ret == 1:
            return True
        elif ret in foo:
            return False
        else:
            foo.add(ret)
            return self.__is_happy(ret, foo)


s = Solution()
print s.isHappy(19)
