package com.company;

import java.util.Arrays;
import java.util.Objects;
import java.util.PriorityQueue;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists!=null){
            ListNode dummy = new ListNode(0), head = dummy;
            PriorityQueue<ListNode> queue = new PriorityQueue<ListNode> ((o1, o2)-> o1.val - o2.val);
            Arrays.stream(lists).filter(Objects::nonNull).forEach(queue::add);

            while(!queue.isEmpty()){
                head.next = queue.poll();
                head = head.next;
                if(head.next!=null){
                    queue.offer(head.next);
                }
            }
            return dummy.next;
        }else{

            return null;
        }
    }
}