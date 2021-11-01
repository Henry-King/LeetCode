import java.util.*;

public class Solution {
    private int[] nums;
    private Map<Integer, Integer> map;
    private Map<Integer, List<List<Integer>>> twoSum;

    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        this.nums = nums;
        map = new HashMap<Integer, Integer>((int) ((float) nums.length / 0.75F + 1.0F));
        twoSum = new HashMap<Integer, List<List<Integer>>>((int) ((float) nums.length * nums.length / 0.75F + 1.0F));
        buildMap();
        buildTwoSum();
        return getSum(0, target, 4);
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
            } else if (operatorNum == 2) {
                List<List<Integer>> twoSumList = twoSum.get(sum);
                if (twoSumList != null) {
                    for (List<Integer> list : twoSumList) {
                        int first = list.get(0);
                        int second = list.get(1);
                        if (first >= left && second >= left) {
                            List<Integer> digit = new LinkedList<Integer>();
                            digit.add(nums[first]);
                            digit.add(nums[second]);
                            result.add(digit);
                        }
                    }
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

    private void buildTwoSum() {
        List<List<Integer>> result;
        List<Integer> list;
        int sum;
        for (int i = nums.length - 1; i >= 0; i--) {
            if (i + 1 <= nums.length - 1 && nums[i + 1] == nums[i])
                continue;
            for (int j = i - 1; j >= 0; j--) {
                if (j + 1 <= i - 1 && nums[j + 1] == nums[j])
                    continue;
                list = new LinkedList<Integer>();
                list.add(j);
                list.add(i);
                sum = nums[i] + nums[j];
                result = twoSum.get(sum);
                if (result == null) {
                    result = new LinkedList<List<Integer>>();
                    twoSum.put(sum, result);
                }
                result.add(list);
            }
        }
    }
}