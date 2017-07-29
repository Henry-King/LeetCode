class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        head, remain, step, left = 1, n, 1, True
        while remain > 1:
            if left or remain % 2 == 1:
                head += step
            step *= 2
            remain /= 2
            left = not left
        return head
