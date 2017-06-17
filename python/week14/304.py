class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix:
            self.accu = [[0] * (len(matrix[0]) + 1) for i in xrange(len(matrix) + 1)]
            for row in xrange(1, len(matrix) + 1):
                for column in xrange(1, len(matrix[0]) + 1):
                    self.accu[row][column] = self.accu[row - 1][column] + self.accu[row][column - 1] \
                                             - self.accu[row - 1][column - 1] + matrix[row - 1][column - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.accu[row2 + 1][col2 + 1] - self.accu[row2 + 1][col1] \
               - self.accu[row1][col2 + 1] + self.accu[row1][col1]



        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

s = NumMatrix([[]])
print s.sumRegion(2, 1, 4, 3)
