class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        column0 = 1
        for i in xrange(len(matrix)):
            if matrix[i][0] == 0:
                column0 = 0
            for j in xrange(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in xrange(len(matrix) - 1, -1, -1):
            for j in xrange(len(matrix[i]) - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if column0 == 0:
                matrix[i][0] = 0
