package com.company;

public class Solution8 {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length-1, mid;
        while(left <= right){
            mid = left+(right-left)/2;
            if(nums[mid] == target){
                return mid;
            }else if(nums[mid] > nums[left]){
                if(target >= nums[left] && target < nums[mid]){
                    right = mid-1;
                }else{
                    left = mid+1;
                }
            }else{
                if(target > nums[mid] && target <= nums[right]){
                    left = mid +1;
                }else{
                    right = mid-1;
                }
            }
        }
        return -1;
    }
}
