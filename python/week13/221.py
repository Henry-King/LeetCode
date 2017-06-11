class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0
        if matrix:
            state = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]
            for i in xrange(1, len(matrix) + 1):
                for j in xrange(1, len(matrix[0]) + 1):
                    if matrix[i - 1][j - 1] == '1':
                        state[i][j] = min(state[i - 1][j], state[i - 1][j - 1], state[i][j - 1]) + 1
                        res = max(res, state[i][j])
        return res * res


s = Solution()
print s.maximalSquare(["10100", "10111", "11111", "10010"])
