class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board and len(board) > 2 and len(board[0]) > 2:
            for i in xrange(len(board)):
                self.dfs(board, i, 0)
                self.dfs(board, i, len(board[i]) - 1)
            for i in xrange(len(board[0])):
                self.dfs(board, 0, i)
                self.dfs(board, len(board) - 1, i)

            for i in xrange(len(board)):
                for j in xrange(len(board[i])):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
            for i in xrange(len(board)):
                for j in xrange(len(board[i])):
                    if board[i][j] == '*':
                        board[i][j] = 'O'

    def dfs(self, board, row, column):
        if board[row][column] == 'O':
            stack = [(row, column)]
            while stack:
                row, column = stack.pop()
                board[row][column] = '*'
                if row + 1 < len(board) and board[row + 1][column] == 'O':
                    stack.append((row + 1, column))
                if row - 1 >= 0 and board[row - 1][column] == 'O':
                    stack.append((row - 1, column))
                if column + 1 < len(board[row]) and board[row][column + 1] == 'O':
                    stack.append((row, column + 1))
                if column - 1 >= 0 and board[row][column - 1] == 'O':
                    stack.append((row, column - 1))


s = Solution()
x = [[u'X', u'X', u'X', u'X'], [u'X', u'O', u'O', u'X'], [u'X', u'X', u'O', u'X'], [u'X', u'O', u'X', u'X']]
s.solve(x)
print x
