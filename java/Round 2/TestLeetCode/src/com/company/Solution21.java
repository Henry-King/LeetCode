package com.company;

import java.util.Arrays;

public class Solution21 {
    public String reorganizeString(String S) {
        int[] frequency = new int[26];
        char[] answer = new char[S.length()];
        for(char letter: S.toCharArray()){
            frequency[letter-'a'] += 100;
        }
        for(char i = 0; i< 26;i++){
            frequency[i] += i;
        }
        Arrays.sort(frequency);

        int index = 0;
        for(int i = 25; i>=0; i--){
            int count = frequency[i]/100;
            char letter = (char) ('a' + frequency[i] % 100);
            if(count > (answer.length+1)/2){
                return "";
            }
            else{
                for(int j=0;j<count;j++){
                    answer[index] = letter;
                    frequency[i]--;
                    index += 2;
                    if(index >= S.length()){
                        index = 1;
                    }
                }
            }
        }
        return new String(answer);
    }
}
