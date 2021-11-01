package com.company;

public class Main {

    public static void main(String[] args) {
        Solution22 solution22 = new Solution22();
        System.out.println(solution22.divide(2147483647, 3));
    }

    static void test(String testCase, WordDictionary wordDictionary) {
        System.out.println(wordDictionary.search(testCase));
    }
}
