class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix and matrix[0]:
            columns = len(matrix[0]) - 1
            lo = 0
            hi = len(matrix) - 1
            while lo <= hi:
                mid = (lo + hi) / 2
                if matrix[mid][columns] > target:
                    hi = mid - 1
                elif matrix[mid][columns] < target:
                    lo = mid + 1
                else:
                    return True

            if lo >= len(matrix):
                return False
            else:
                column = matrix[lo]
                lo = 0
                hi = columns
                while lo < hi:
                    mid = (lo + hi) / 2
                    if column[mid] > target:
                        hi = mid - 1
                    elif column[mid] < target:
                        lo = mid + 1
                    else:
                        return True

                return column[lo] == target
        else:
            return False


s = Solution()
print s.searchMatrix([
    [1]
], 2)
