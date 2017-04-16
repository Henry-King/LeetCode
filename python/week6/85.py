class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix and matrix[0]:
            row_count = len(matrix)
            column_count = len(matrix[0])
            h = [0] * (column_count + 1)
            j = max_area = 0

            for i in xrange(row_count):
                stack = []
                for j in xrange(column_count + 1):
                    if j < column_count:
                        if matrix[i][j] == '1':
                            h[j] += 1
                        else:
                            h[j] = 0

                    if not stack or h[j] >= h[stack[len(stack) - 1]]:
                        stack.append(j)
                    else:
                        while stack and h[j] < h[stack[len(stack) - 1]]:
                            top = h[stack.pop()]
                            width = (j - 1 - stack[len(stack) - 1]) if stack else j
                            max_area = max(top * width, max_area)
                        stack.append(j)
            return max_area
        else:
            return 0


s = Solution()
print s.maximalRectangle(["10100", "10111", "11111", "10010"])
