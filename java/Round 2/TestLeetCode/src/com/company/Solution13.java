package com.company;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class Solution13 {
    private int min_num;
    private Set<String> sets;

    public List<String> removeInvalidParentheses(String s) {
        sets = new HashSet<>();
        min_num = Integer.MAX_VALUE;
        removeInvalidParentheses(s, 0, 0, 0, 0, new ArrayList<>(s.length()));
        return new ArrayList<>(sets);
    }

    private void removeInvalidParentheses(String s, int left_count, int right_count, int removed_parentheses, int index, List<Character> result) {
        if (index == s.length()) {
            if (left_count == right_count) {
                if (removed_parentheses < min_num) {
                    min_num = removed_parentheses;
                    sets.clear();
                }
                if (removed_parentheses <= min_num) {
                    sets.add(result.stream().map(Object::toString).collect(Collectors.joining()));
                }
            }
        } else {
            char letter = s.charAt(index);
            if (letter == '(' || letter == ')') {
                removeInvalidParentheses(s, left_count, right_count, removed_parentheses + 1, index + 1, result);
            }

            if (right_count <= left_count) {
                int size = result.size();
                result.add(letter);
                if (letter == '(') {
                    removeInvalidParentheses(s, left_count + 1, right_count, removed_parentheses, index + 1, result);
                } else if (letter == ')') {
                    removeInvalidParentheses(s, left_count, right_count + 1, removed_parentheses, index + 1, result);
                } else {
                    removeInvalidParentheses(s, left_count, right_count, removed_parentheses, index + 1, result);
                }
                result.remove(size);
            }
        }
    }
}
