class Solution(object):
    full_set = set([str(i) for i in xrange(1, 10)])

    def __init__(self):
        """
        Change to Tuple
        """
        self.rows = ([set() for i in xrange(0, 9)])
        self.columns = ([set() for i in xrange(0, 9)])
        self.matrix = ([set() for i in xrange(0, 9)])

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in xrange(len(board)):
            board[i] = list(board[i])

        start = None
        for row in xrange(len(board)):
            for column in xrange(len(board[0])):
                if board[row][column] != '.':
                    self.__set_value(column, row, board[row][column])
                else:
                    if not start:
                        start = (row, column)

        self.__try_solveSudoku(board, start[0], start[1])

        for i in xrange(len(board)):
            board[i] = "".join(board[i])

    def __try_solveSudoku(self, board, last_row, last_column):
        for row in xrange(last_row, 9):
            start_column = last_column if row == last_row else 0
            for column in xrange(start_column, 9):
                if board[row][column] == '.':
                    diff = Solution.full_set - self.rows[row] - self.columns[column] - self.matrix[
                        row / 3 * 3 + column / 3]
                    if diff:
                        for value in diff:
                            self.__set_value(column, row, value)
                            board[row][column] = str(value)
                            ret = self.__try_solveSudoku(board, row, column)
                            if ret:
                                return True
                            else:
                                self.__reset_value(board, column, row, value)
                        return False
                    else:
                        return False
        return True

    def __reset_value(self, board, column, row, value):
        self.rows[row].remove(value)
        self.columns[column].remove(value)
        self.matrix[row / 3 * 3 + column / 3].remove(value)
        board[row][column] = '.'

    def __set_value(self, column, row, value):
        self.rows[row].add(value)
        self.columns[column].add(value)
        self.matrix[row / 3 * 3 + column / 3].add(value)


s = Solution()
matrix = ["..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6",
          "...2759.."]
s.solveSudoku(matrix)
print matrix
