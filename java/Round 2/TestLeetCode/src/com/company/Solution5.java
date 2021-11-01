package com.company;

import java.util.*;
import java.util.stream.IntStream;

public class Solution5 {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        Map<String, String> emailToName = new HashMap<>();
        Map<String, Integer> emailToId = new HashMap<>();
        DisjointSet dsu = new DisjointSet();
        int index = 0;

        for(List<String> account: accounts){
            String name = account.get(0);
            for(String email: account.subList(1, account.size())){
                emailToName.put(email, name);
                if(!emailToId.containsKey(email)){
                    emailToId.put(email, index++);
                }
                dsu.union(emailToId.get(email), emailToId.get(account.get(1)));
            }
        }

        Map<Integer, List<String>> ans = new HashMap<>();
        for(String email: emailToId.keySet()){
            int root = dsu.find(emailToId.get(email));
            ans.computeIfAbsent(root, key-> new LinkedList<>()).add(email);
        }

        for(List<String> values: ans.values()){
            Collections.sort(values);
            values.add(0, emailToName.get(values.get(0)));
        }
        return new ArrayList<>(ans.values());
    }

    static class DisjointSet{
        private final int[] parent;
        private final int[] rank;
        DisjointSet(){
            parent = IntStream.iterate(0, seed-> seed+1).limit(10001).toArray();
            rank = new int[10001];
        }

        public void union(int x, int y){
            link(find(x), find(y));
        }

        public int find(int x){
            if(x!=parent[x]){
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        private void link(int x, int y){
            if(rank[x] < rank[y]){
                parent[x] = y;
            }else{
                parent[y] = x;
                if(rank[x] == rank[y]){
                    rank[x]++;
                }
            }
        }
    }
}
