package com.company;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.stream.Collectors;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class Solution14 {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        LinkedList<Integer> list = new LinkedList<>();
        serialize(root, list);
        return list.stream().map(i-> i == null ? "null" : Integer.toString(i)).collect(Collectors.joining(","));
    }

    private void serialize(TreeNode root, List<Integer> list){
        if(root!=null){
            list.add(root.val);
            serialize(root.left, list);
            serialize(root.right, list);
        }else{
            list.add(null);
        }
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        return deserializeImp(Arrays.stream(data.split(","))
                .map(i-> "null".equals(i) ? null : Integer.valueOf(i))
                .collect(Collectors.toCollection(LinkedList::new)));
    }

    private TreeNode deserializeImp(Queue<Integer> queue) {
        Integer value = queue.poll();
        if(value == null){
            return null;
        }else{
            TreeNode ret = new TreeNode(value);
            ret.left = deserializeImp(queue);
            ret.right = deserializeImp(queue);
            return ret;
        }
    }
}
