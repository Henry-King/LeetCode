class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        else:
            row = 0
            column = len(matrix[0]) - 1
            while column >= 0 and row < len(matrix):
                if matrix[row][column] == target:
                    return True
                elif matrix[row][column] > target:
                    column -= 1
                else:
                    row += 1
            return False


s = Solution()

print s.searchMatrix([
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
], 20)
