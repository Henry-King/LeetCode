class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in xrange(len(matrix)):
            for j in xrange(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


s = Solution()
matrix = [[1, 2], [3, 4]]
s.rotate(matrix)
print matrix
