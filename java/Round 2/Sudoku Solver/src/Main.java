import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        char[][] source = new char[][]{
                "..9748...".toCharArray(),
                "7........".toCharArray(),
                ".2.1.9...".toCharArray(),
                "..7...24.".toCharArray(),
                ".64.1.59.".toCharArray(),
                ".98...3..".toCharArray(),
                "...8.3.2.".toCharArray(),
                "........6".toCharArray(),
                "...2759..".toCharArray()};
        Solution solution = new Solution();
        solution.solveSudoku(source);
        System.out.println(Arrays.deepToString(source));
    }
}
