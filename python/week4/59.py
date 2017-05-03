class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = [[0 for i in xrange(n)] for i in xrange(n)]
        top, left = 0, 0
        count = 1
        bottom, right = n - 1, n - 1

        while True:
            for column in xrange(left, right + 1):
                ret[top][column] = count
                count += 1
            top += 1
            if top > bottom:
                break

            for row in xrange(top, bottom + 1):
                ret[row][right] = count
                count += 1
            right -= 1
            if left > right:
                break

            for column in xrange(right, left - 1, -1):
                ret[bottom][column] = count
                count += 1
            bottom -= 1
            if top > bottom:
                break

            for row in xrange(bottom, top - 1, -1):
                ret[row][left] = count
                count += 1
            left += 1
            if left > right:
                break

        return ret


s = Solution()
print s.generateMatrix(0)
