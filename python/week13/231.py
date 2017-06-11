class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        else:
            return not n & n - 1


s = Solution()
print s.isPowerOfTwo(5)
