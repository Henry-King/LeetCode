class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board:
            for row in xrange(0, len(board)):
                for column in xrange(0, len(board[row])):
                    if word[0] == board[row][column] and self.__dfs(board, word, [(row, column)]):
                        return True
            return False
        else:
            return False

    def __dfs(self, board, word, loc_in_board):
        if len(loc_in_board) == len(word):
            return True

        else:
            cur_row, cur_column = loc_in_board[len(loc_in_board) - 1]
            if self.__search(board, loc_in_board, (cur_row + 1, cur_column), word):
                return True
            if self.__search(board, loc_in_board, (cur_row - 1, cur_column), word):
                return True
            if self.__search(board, loc_in_board, (cur_row, cur_column + 1), word):
                return True
            if self.__search(board, loc_in_board, (cur_row, cur_column - 1), word):
                return True
            return False

    def __search(self, board, loc_in_board, new_loc, word):
        if 0 <= new_loc[0] < len(board) and 0 <= new_loc[1] < len(board[new_loc[0]]) and \
                                new_loc not in loc_in_board and \
                                board[new_loc[0]][new_loc[1]] == word[len(loc_in_board)]:
            loc_in_board.append(new_loc)
            if self.__dfs(board, word, loc_in_board):
                return True
            else:
                loc_in_board.pop()
        return False


s = Solution()
print s.exist([["aa"]], "aaa")
