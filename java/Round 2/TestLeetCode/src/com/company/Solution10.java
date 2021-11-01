package com.company;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution10 {
    public String minRemoveToMakeValid(String s) {
        LinkedList<Integer> stack = new LinkedList<>();
        Set<Integer> filter = new HashSet<>();
        for (int i = 0; i < s.length(); i++) {
            char letter = s.charAt(i);
            if (letter == '(') {
                stack.push(i);
            } else if (letter == ')') {
                if (!stack.isEmpty()) {
                    stack.pop();
                } else {
                    filter.add(i);
                }
            }
        }

        filter.addAll(stack);
        return IntStream.range(0, s.length())
                .filter(i -> !filter.contains(i))
                .mapToObj(s::charAt)
                .map(Object::toString)
                .collect(Collectors.joining());
    }
}
