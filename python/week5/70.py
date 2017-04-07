class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        else:
            one_back = 1
            two_back = 1
            for i in xrange(2, n + 1):
                cur = one_back + two_back
                two_back = one_back
                one_back = cur
            return one_back


s = Solution()
print s.climbStairs(2)
