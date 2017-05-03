class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # if n > 0:
        #     ret = [[]]
        #     for i in xrange(n):
        #         reflected = ret[:]
        #         reflected.reverse()
        #         ret = [['0'] + item for item in ret]
        #         reflected = [['1'] + item for item in reflected]
        #         ret.extend(reflected)
        #     ret = [int("".join(item), 2) for item in ret]
        #     return ret
        # else:
        #     return [0]
        ret = []
        for index in xrange(2 ** n):
            ret.append(index ^ (index >> 1))
        return ret


s = Solution()
print s.grayCode(2)
