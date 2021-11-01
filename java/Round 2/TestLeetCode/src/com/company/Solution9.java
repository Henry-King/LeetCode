package com.company;

import java.util.*;

class Solution9 {
    public boolean isBipartite(int[][] graph) {
        Map<Integer, List<Integer>> map = initMap(graph);
        Set<Integer> a = new HashSet<>();
        Set<Integer> b = new HashSet<>();
        Set<Integer> aVertex = new HashSet<>();
        Set<Integer> bVertex = new HashSet<>();

        while(!map.isEmpty()){
            if(aVertex.isEmpty()){
                Integer start = map.keySet().iterator().next();
                aVertex.add(start);
            }

            for(Integer vertex: aVertex){
                if(b.contains(vertex)){
                    return false;
                }else{
                    a.add(vertex);
                    if(map.containsKey(vertex)){
                        bVertex.addAll(map.get(vertex));
                    }
                    map.remove(vertex);
                }
            }
            aVertex.clear();

            Set<Integer> temp = a;
            a = b;
            b = temp;

            temp = aVertex;
            aVertex = bVertex;
            bVertex = temp;
        }
        return true;
    }

    private Map<Integer, List<Integer>> initMap(int[][] graph){
        Map<Integer, List<Integer>> map = new HashMap<>();
        for(int i=0;i<graph.length;i++){
            List<Integer> list = new ArrayList(graph[i].length);
            for(int j: graph[i]){
                list.add(j);
            }
            map.put(i, list);
        }
        return map;
    }
}