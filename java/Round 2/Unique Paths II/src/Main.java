public class Main {

    public static void main(String[] args) {
        int[][] martrix =new int[][]{
                {0,0,0},
                {0,1,0},
                {0,0,0}};
        Solution solution =new Solution();
        int result = solution.uniquePathsWithObstacles(martrix);
        System.out.println(result);
    }
}
