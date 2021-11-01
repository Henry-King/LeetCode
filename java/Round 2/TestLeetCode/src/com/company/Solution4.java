package com.company;

import javafx.util.Pair;

import java.util.*;

public class Solution4 {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        //Map<Email, Pair<Name, PriorityQueue<Email>>>
        Map<String, Pair<String, PriorityQueue<String>>> map = new HashMap<>();

        for(List<String> account: accounts){
            PriorityQueue<String> queue = new PriorityQueue<>();
            PriorityQueue<String> previousQueue = null;
            String name = account.get(0);
            Set<String> emails = new HashSet<>(account.subList(1, account.size()));

            for(String email: emails){
                if(map.containsKey(email)){
                    if(previousQueue == null){
                        previousQueue = map.get(email).getValue();
                    }else{
                        PriorityQueue<String> assocQueue = map.get(email).getValue();
                        while(assocQueue!= previousQueue && !assocQueue.isEmpty()){
                            String assocEmail = assocQueue.poll();
                            previousQueue.offer(assocEmail);
                            map.put(assocEmail, new Pair<>(name, previousQueue));
                        }
                    }
                }else{
                    queue.offer(email);
                }
            }

            if(previousQueue!=null){
                while(!queue.isEmpty()){
                    previousQueue.offer(queue.poll());
                }
                queue = previousQueue;
            }

            for(String email: emails){
                map.put(email, new Pair<>(name, queue));
            }
        }

        Set<Pair<String, PriorityQueue<String>>> set=new HashSet<>(map.values());
        List<List<String>> answer = new LinkedList<>();
        for(Pair<String, PriorityQueue<String>> pair: set){
            List<String> list = new LinkedList<>();
            list.add(pair.getKey());
            while(!pair.getValue().isEmpty()){
                list.add(pair.getValue().poll());
            }
            answer.add(list);
        }
        return answer;
    }
}
