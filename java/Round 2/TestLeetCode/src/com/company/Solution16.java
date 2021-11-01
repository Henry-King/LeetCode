package com.company;

import java.util.HashMap;
import java.util.Map;

public class Solution16 {
    //"aa", 1
    //"eceba", 2
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        Map<Character, Integer> map = new HashMap<>();
        int left = 0, right=0, max= Math.min(k, s.length());

        while(right < s.length()){
            int unique = map.size();
            if(unique > k){
                map.compute(s.charAt(left++), (key,v)-> v == 1 ? null : v-1);
            }else{
                max = Math.max(max, right-left);
                map.compute(s.charAt(right++), (key,v)-> v == null? 1 : v+1);
            }
        }
        if(map.size()<=k){
            max=Math.max(max, right-left);
        }
        return max;
    }
}
