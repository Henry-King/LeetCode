import java.util.*;

public class Solution {
    private int[] nums;
    private Map<Integer, Integer> map;

    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        this.nums = nums;
        map = new HashMap<Integer, Integer>((int) ((float) nums.length / 0.75F + 1.0F));
        buildMap();
        return getSum(0, 0, 3);
    }

    private List<List<Integer>> getSum(int left, int sum, int operatorNum) {
        List<List<Integer>> result = new LinkedList<List<Integer>>();
        for (int i = left; i < nums.length; i++) {
            if (operatorNum == 1) {
                Integer value = map.get(sum);
                if (value != null && value >= left) {
                    List<Integer> digit = new LinkedList<Integer>();
                    digit.add(nums[value]);
                    result.add(digit);
                }
                break;
            } else {
                if (i - 1 >= left && nums[i] == nums[i - 1]) {
                    continue;
                }
                List<List<Integer>> sums = getSum(i + 1, sum - nums[i], operatorNum - 1);
                for (List<Integer> list : sums)
                    list.add(0, nums[i]);
                result.addAll(sums);
            }
        }
        return result;
    }


    private void buildMap() {
        for (int i = 0; i < nums.length; i++)
            map.put(nums[i], i);
    }
}