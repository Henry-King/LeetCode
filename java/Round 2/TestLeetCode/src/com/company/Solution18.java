package com.company;

public class Solution18 {
    public void nextPermutation(int[] nums) {
        int i;
        for(i=nums.length-1;i>0;i--){
            if(nums[i]>nums[i-1]){
                break;
            }
        }

        if(i>0){
            int j = nums.length-1;
            while(nums[j]<=nums[i-1]){
                j--;
            }
            swap(nums, j, i-1);
        }
        int left = i, right = nums.length-1;
        while(left<right){
            swap(nums, left++, right--);
        }
    }

    public void swap(int nums[],int index_a, int index_b){
        int temp = nums[index_a];
        nums[index_a] = nums[index_b];
        nums[index_b] = temp;
    }
}
