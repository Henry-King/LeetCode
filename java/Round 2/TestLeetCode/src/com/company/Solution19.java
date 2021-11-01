package com.company;

import java.util.Arrays;
import java.util.List;

public class Solution19 {
    public int[] exclusiveTime(int n, List<String> logs) {
        int[] answer = new int[n];
        int pre_id = -1, pre_start = -1, pre_end = -1;
        Arrays.fill(answer, 0);
        for(String log: logs){
            String[] info = log.split(":");
            int id = Integer.parseInt(info[0]);
            int timeStamp = Integer.parseInt(info[2]);
            if("start".equals(info[1])){
                if(pre_id != -1){
                    answer[pre_id] = timeStamp - pre_start;
                }
                pre_id = id;
                pre_start = timeStamp;
            }else{
                if(pre_id == id){
                    answer[id] += timeStamp - pre_start+1;
                    pre_id = -1;
                    pre_start = -1;
                }else{
                    answer[id] += timeStamp-pre_end;
                }
                pre_end = timeStamp;
            }
        }
        return answer;
    }
}
