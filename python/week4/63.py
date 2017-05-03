class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]:
            return 0
        else:
            rows = len(obstacleGrid)
            columns = len(obstacleGrid[0])
            for i in xrange(rows):
                for j in xrange(columns):
                    if obstacleGrid[i][j] == 1:
                        obstacleGrid[i][j] = 0
                    elif not i and not j:
                        obstacleGrid[i][j] = 1
                    elif not i:
                        obstacleGrid[i][j] = obstacleGrid[i][j - 1]
                    elif not j:
                        obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]
            return obstacleGrid[rows - 1][columns - 1]


s = Solution()
print s.uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])
