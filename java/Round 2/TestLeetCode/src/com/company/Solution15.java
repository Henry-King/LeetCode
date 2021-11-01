package com.company;

import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

class Solution15 {
    private List<String> answer;
    private String num;
    private int target;
    public List<String> addOperators(String num, int target) {
        this.num = num;
        this.target = target;
        answer = new LinkedList<>();
        LinkedList<String> exp = new LinkedList<>();
        backtracking(0, 0, 0, 0, exp);
        return answer;
    }

    private void backtracking(int index, long previousOp, long currentOp, long previousExpValue, LinkedList<String> exp){
        if(index == num.length()){
            if(previousExpValue == target && currentOp == 0){
                answer.add(exp.stream().skip(1).collect(Collectors.joining()));
            }
        }else{
            currentOp = Character.getNumericValue(num.charAt(index)) + currentOp * 10;
            String op_string = Long.toString(currentOp);

            if(currentOp > 0){
                backtracking(index+1, previousOp, currentOp, previousExpValue, exp);
            }

            exp.add("+");
            exp.add(op_string);
            backtracking(index+1, currentOp, 0, previousExpValue + currentOp, exp);
            exp.removeLast();
            exp.removeLast();

            if(exp.size()>0){
                exp.add("-");
                exp.add(op_string);
                backtracking(index+1, -currentOp, 0, previousExpValue - currentOp, exp);
                exp.removeLast();
                exp.removeLast();

                exp.add("*");
                exp.add(op_string);
                backtracking(index+1, currentOp*previousOp, 0, previousExpValue - previousOp + previousOp * currentOp, exp);
                exp.removeLast();
                exp.removeLast();
            }
        }
    }
}