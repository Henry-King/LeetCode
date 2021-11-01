package com.company;

import java.util.*;
import java.util.stream.Collectors;

public class Solution12 {
    public String alienOrder(String[] words) {
        if(words.length > 1){
            Map<Character, Set<Character>> order = new HashMap<>();
            Map<Character, Integer> inBounds = new HashMap<>();
            intMaps(words, order, inBounds);
            List<Character> answer = topologicalSort(order, inBounds);
            return answer.stream().map(Object::toString).collect(Collectors.joining());
        }
        else{
            return words[0];
        }
    }

    private void intMaps(String[] words, Map<Character, Set<Character>> order, Map<Character, Integer> inBounds){
        words[0].chars().mapToObj(e->(char)e).forEach(e->inBounds.computeIfAbsent(e, k-> 0));
        for(int i=1;i<words.length;i++){
            String previous = words[i-1];
            String current = words[i];
            current.chars().mapToObj(e->(char)e).forEach(e->inBounds.computeIfAbsent(e, k-> 0));
            int j, min = Math.min(previous.length(), current.length());
            for(j=0; j< min; j++){
                char previous_letter = previous.charAt(j);
                char current_letter = current.charAt(j);
                if(previous_letter != current_letter){
                    if(!order.computeIfAbsent(previous_letter, k->new HashSet<>()).contains(current_letter)){
                        order.get(previous_letter).add(current_letter);
                        inBounds.computeIfPresent(current_letter, (k,v)-> v+1);
                    }
                    break;
                }
            }
            if(j == min && previous.length() > current.length()){
                inBounds.clear();
            }
        }
    }

    private List<Character> topologicalSort(Map<Character, Set<Character>> order, Map<Character, Integer> inBounds){
        List<Character> answer = new LinkedList<>();
        if(!inBounds.isEmpty()){
            LinkedList<Character> list = inBounds.entrySet().stream()
                    .filter(e -> e.getValue() == 0).map(Map.Entry::getKey)
                    .collect(Collectors.toCollection(LinkedList::new));

            while(!list.isEmpty()){
                char vertex = list.pop();
                answer.add(vertex);
                Set<Character> dominatedChars = order.remove(vertex);
                if(dominatedChars!=null){
                    for(char dominated:dominatedChars){
                        if(inBounds.get(dominated) == 1){
                            list.push(dominated);
                        }
                        inBounds.computeIfPresent(dominated, (k,v)->v-1);
                    }
                }
            }
            if(!order.isEmpty()){
                answer.clear();
            }
        }
        return answer;
    }
}
