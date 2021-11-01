package com.company;

import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

public class Solution11 {
    public int[][] kClosest(int[][] points, int K) {
        sort(points, 0, points.length-1, K);
        return Arrays.copyOf(points, K);
    }

    private void sort(int[][] points, int start, int end, int K){
        int pivot = partition(points, start, end);
        if(pivot<K){
            sort(points, pivot+1, end, K-pivot);
        }else if(pivot > K){
            sort(points, start, pivot-1, K);
        }
    }

    private int partition(int[][] points, int start, int end){
        int pivot_index = ThreadLocalRandom.current().nextInt(start, end+1);
        int[] pivot = points[pivot_index];
        swap(points, pivot_index, end);
        int pointer = start;

        for(int i=start; i< end; i++){
            if(dinstanceToOrigin(points[i]) <=  dinstanceToOrigin(pivot)){
                swap(points, i, pointer);
                pointer++;
            }
        }

        swap(points, pointer, end);
        return pointer;
    }

    private int dinstanceToOrigin(int[] a){
        return a[0]*a[0] + a[1]*a[1];
    }

    private void swap(int[][] points, int a, int b){
        int[] temp = points[a];
        points[a] = points[b];
        points[b] = temp;
    }
}
