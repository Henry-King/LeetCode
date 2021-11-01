import java.util.ArrayList;
import java.util.List;

public class Solution {
    public int[] plusOne(int[] digits) {
        int add=1,sum;
        List<Integer> list =new ArrayList<Integer>(digits.length+1);
        for(int i=digits.length-1;i>=0;i--){
            sum = digits[i]+add;
            add = sum>=10?1:0;
            sum %=10;
            list.add(0,sum);
        }
        if(add ==1)
            list.add(0,add);
        int[] result= new int[list.size()];
        for(int i=0;i<list.size();i++)
            result[i]= list.get(i);
        return  result;
    }
}