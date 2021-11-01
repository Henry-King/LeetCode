package com.company;

import java.util.*;
import java.util.stream.Collectors;

class Solution2 {
    public int leastInterval(char[] tasks, int n) {
        int answer = 0;
        Map<Character, Integer> map = new HashMap();
        for (char letter : tasks) {
            map.merge(letter, 1, (oldValue,initValue)->oldValue+1);
        }
        return answer;
    }

    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> nums1_set = Arrays.stream(nums1).boxed().collect(Collectors.toSet());
        Set<Integer> nums2_set = Arrays.stream(nums2).boxed().collect(Collectors.toSet());
        nums1_set.retainAll(nums2_set);
        return new ArrayList<Integer>(nums1_set).stream().mapToInt(i->i).toArray();
    }
}