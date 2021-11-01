public class Solution {
    private int benchmark[][];

    public int uniquePaths(int m, int n) {
        benchmark = new int[m][n];
        for(int i=0;i<m;i++) {
            benchmark[i] = new int[n];
            for(int j=0;j<n;j++)
                benchmark[i][j] = 1;
        }
        if(m>1&&n>1) {
            for (int i = 1; i < m; i++)
                for (int j = 1; j < n; j++) {
                    benchmark[i][j]=benchmark[i-1][j]+benchmark[i][j-1];
                }
        }
        return benchmark[m-1][n-1];
    }
}