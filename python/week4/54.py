class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])


s = Solution()
print s.spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
