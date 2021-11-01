import java.util.Arrays;

public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int left, right, sum, closet;
        Arrays.sort(nums);
        closet = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < nums.length - 2; i++) {
            left = i + 1;
            right = nums.length - 1;
            while (left < right) {
                if ((sum = nums[i] + nums[left] + nums[right]) == target)
                    return target;
                else if (sum > target) {
                    if (Math.abs(target - sum) < Math.abs(target - closet))
                        closet = sum;
                    do {
                        right--;
                    } while (left < right && nums[right] == nums[right + 1]);
                } else {
                    if (Math.abs(target - sum) < Math.abs(target - closet))
                        closet = sum;
                    do {
                        left++;
                    } while (left < right && nums[left] == nums[left - 1]);
                }
            }
        }
        return closet;
    }
}