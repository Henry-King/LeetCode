class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = []
        columns = []
        sub_boxes = []
        for i in range(9):
            rows.append(set())
            columns.append(set())
            sub_boxes.append(set())

        for row_index, row_str in enumerate(board):
            for column_index, char in enumerate(row_str):
                if char == '.':
                    pass
                elif len(char) == 1 and char.isdigit():
                    row_set = rows[row_index]
                    column_set = columns[column_index]
                    box_set = sub_boxes[row_index/3*3 + column_index/3]
                    if char in row_set:
                        return False
                    else:
                        row_set.add(char)

                    if char in column_set:
                        return False
                    else:
                        column_set.add(char)

                    if char in box_set:
                        return False
                    else:
                        box_set.add(char)
                else:
                    return False
        return True


s = Solution()
print s.isValidSudoku(
    [".87654321", "2........", "3........", "4........", "5........", "6........", "7........", "8........",
     "9........"])
