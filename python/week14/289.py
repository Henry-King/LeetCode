class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        0, dead
        1, live
        2, dead to live
        3, live to dead
        """
        for row in xrange(len(board)):
            for column in xrange(len(board[row])):
                livingNeighbor = Solution.__livingNeighborNum(board, row, column)
                if board[row][column] == 1:
                    if livingNeighbor < 2 or livingNeighbor > 3:
                        board[row][column] = 3
                else:
                    if livingNeighbor == 3:
                        board[row][column] = 2

        for row in xrange(len(board)):
            for column in xrange(len(board[row])):
                if board[row][column] == 2:
                    board[row][column] = 1
                elif board[row][column] == 3:
                    board[row][column] = 0

    @staticmethod
    def __livingNeighborNum(board, row, column):
        neighbors = [row and column and Solution.__isLiving(board[row - 1][column - 1]),
                     row and Solution.__isLiving(board[row - 1][column]),
                     row and column + 1 < len(board[row]) and Solution.__isLiving(board[row - 1][column + 1]),
                     column and Solution.__isLiving(board[row][column - 1]),
                     column + 1 < len(board[row]) and Solution.__isLiving(board[row][column + 1]),
                     row + 1 < len(board) and column and Solution.__isLiving(board[row + 1][column - 1]),
                     row + 1 < len(board) and Solution.__isLiving(board[row + 1][column]),
                     row + 1 < len(board) and column + 1 < len(board[row]) and
                     Solution.__isLiving(board[row + 1][column + 1])]
        return neighbors.count(True)

    @staticmethod
    def __isLiving(cell):
        return cell == 1 or cell == 3


matrix = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
s = Solution()
s.gameOfLife(matrix)
print matrix
