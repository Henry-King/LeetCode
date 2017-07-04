class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            product = 1
            while n > 4:
                product *= 3
                n -= 3
            product *= n
            return product
