public class Solution {
    public int missingNumber(int[] nums) {
        int partial=0;
        for(int num:nums)
            partial+=num;
        int complete=nums.length*(nums.length+1)/2;
        return complete-partial;
    }
}