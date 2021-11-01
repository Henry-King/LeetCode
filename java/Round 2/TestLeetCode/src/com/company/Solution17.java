package com.company;

import javafx.util.Pair;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.stream.Collectors;

public class Solution17 {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        Map<Integer, Map<Pair<Integer, Long>, Integer>> answer = new TreeMap<>();
        verticalOrder(root, 0, 0, answer);
        return answer.values().stream().map(e -> new ArrayList<>(e.values())).collect(Collectors.toList());
    }

    private void verticalOrder(TreeNode root, int x, int y, Map<Integer, Map<Pair<Integer, Long>, Integer>> answer) {
        if (root != null) {
            answer.computeIfAbsent(x, k -> new TreeMap<>((pair1, pair2) ->
                    pair1.getKey().equals(pair2.getKey()) ?
                            Long.compare(pair1.getValue(), pair2.getValue()) :
                            Integer.compare(pair1.getKey(), pair2.getKey())))
                    .put(new Pair<>(y, System.currentTimeMillis()), root.val);
            verticalOrder(root.left, x - 1, y + 1, answer);
            verticalOrder(root.right, x + 1, y + 1, answer);
        }
    }
}
