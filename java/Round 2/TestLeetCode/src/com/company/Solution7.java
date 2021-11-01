package com.company;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class Solution7 {
    public int[][] merge(int[][] intervals) {
        if(intervals.length  > 1){
            Arrays.sort(intervals, (t1, t2)-> t1[0] - t2[0]);
            Deque<int[]> stack = new ArrayDeque(intervals.length);
            stack.push(intervals[0]);
            for(int i = 1; i<intervals.length;i++){
                int[] interval = intervals[i];
                if(isOverlapping(interval, stack.peek())){
                    stack.push(mergeInterval(interval, stack.pop()));
                }
            }
            return stack.toArray(new int[0][]);
        }
        else{
            return intervals;
        }
    }

    private boolean isOverlapping(int[] foo, int[] bar){
        return Math.max(foo[0], bar[0]) <= Math.min(foo[1], bar[1]);
    }

    private int[] mergeInterval(int[] foo, int[] bar){
        return new int[]{Math.min(foo[0], bar[0]), Math.max(foo[1], bar[1])};
    }
}
