package com.company;

import java.util.stream.IntStream;

public class Solution6 {
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        int[] sums = new int[nums.length-k+1];
        int sum = 0;
        //sums: 3, 3, 3, 8, 13, 12, 6
        for(int i = 0; i< nums.length;i++){
            sum += nums[i];
            if(i>=k){
                sum -= nums[i-k];
            }
            if(i >= k-1){
                sums[i+1-k] = sum;
            }
        }

        //left: 0, 0, 0, 3, 4, 4, 4
        int[] left = new int[sums.length];
        int best = 0;
        for(int i=0;i<left.length;i++){
            if(sums[i] > sums[best]){
                best = i;
            }
            left[i] = best;
        }

        //right: 4, 4, 4, 4, 4, 5, 6
        int[] right = new int[sums.length];
        best = right.length-1;
        for(int i = right.length-1; i>=0;i--){
            if(sums[i] >= sums[best]){
                best = i;
            }
            right[i] = best;
        }

        int[] answer = new int[]{-1,-1,-1};
        //i=2; i< 5
        //0, 2, 4
        //0, 3, 5
        //0, 4, 6
        for(int i=k; i< sums.length-k; i++){
            if(answer[0] == -1 || IntStream.of(answer).map(index->sums[index]).sum()
                    < IntStream.of(sums[left[i-k]], sums[i], sums[right[i+k]]).sum()){
                answer[0] = left[i-k];
                answer[1] = i;
                answer[2] = right[i+k];
            }
        }
        return answer;
    }
}
