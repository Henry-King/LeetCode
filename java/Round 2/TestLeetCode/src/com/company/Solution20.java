package com.company;

import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class Solution20 {
    public int[] findDiagonalOrder(int[][] matrix) {
        if(matrix.length > 0){
            List<Integer> answer = new LinkedList<>();
            int rows = matrix.length, columns = matrix[0].length;
            boolean odd = true;
            for(int i=0;i<rows+columns-2;i++){
                int row = i < rows ? i : rows-1;
                int column = i < rows ? 0 : i - rows + 1;
                List<Integer> temp = new LinkedList<>();
                while(row >=0 && column < columns){
                    temp.add(matrix[row--][column++]);
                }

                if(!odd){
                    Collections.reverse(temp);
                }
                odd = !odd;
                answer.addAll(temp);
            }
            return answer.stream().mapToInt(i->i).toArray();
        }
        else{
            return new int[0];
        }
    }
}
