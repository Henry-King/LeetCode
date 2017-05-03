class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        columns = len(grid[0])

        for i in xrange(rows):
            for j in xrange(columns):
                if not i and not j:
                    pass
                elif not i:
                    grid[i][j] += grid[i][j - 1]
                elif not j:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[rows-1][columns-1]

