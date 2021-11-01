public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int rows = obstacleGrid.length;
        int columns = obstacleGrid[0].length;
        int[][] paths = new int[rows][];
        for (int i = 0; i < rows; i++)
            paths[i] = new int[columns];
        if (obstacleGrid[rows - 1][columns - 1] == 1)
            return 0;
        else {
            paths[rows - 1][columns - 1] = 1;
            for (int i = columns - 2; i >= 0; i--) {
                if (paths[rows - 1][i + 1] == 0)
                    paths[rows - 1][i] = 0;
                else
                    paths[rows - 1][i] = obstacleGrid[rows - 1][i] == 1 ? 0 : 1;
            }
            for (int i = rows - 2; i >= 0; i--) {
                if (paths[i + 1][columns - 1] == 0)
                    paths[i][columns - 1] = 0;
                else
                    paths[i][columns - 1] = obstacleGrid[i][columns - 1] == 1 ? 0 : 1;
            }
            for (int i = rows - 2; i >= 0; i--)
                for (int j = columns - 2; j >= 0; j--) {
                    if (obstacleGrid[i][j] == 1)
                        paths[i][j] = 0;
                    else
                        paths[i][j] = paths[i + 1][j] + paths[i][j + 1];
                }
            return paths[0][0];
        }
    }
}