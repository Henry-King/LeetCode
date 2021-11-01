import java.util.List;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<List<Integer>> result = solution.combinationSum(new int[]{3,12,9,11,6,7,8,5,4},15);
        System.out.println(result);
    }
}
