package com.company;

public class WordDictionary {
    private TrieNode root;
    /** Initialize your data structure here. */
    public WordDictionary() {
        root = new TrieNode();
    }

    /** Adds a word into the data structure. */
    public void addWord(String word) {
        TrieNode current = root;
        for(char letter: word.toCharArray()){
            if(!current.contains(letter)){
                current.put(letter);
            }
            current = current.get(letter);
        }
        current.setEnd(true);
    }

    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    public boolean search(String word) {
        return backtracking(word, 0, root);
    }

    private boolean backtracking(String word, int start, TrieNode pointer){
        for(int i=start;i<word.length();i++){
            char value = word.charAt(i);
            if(value=='.'){
                for(char letter = 'a'; letter<='z';letter++){
                    if(pointer.contains(letter) && backtracking(word, i+1, pointer.get(letter))){
                        return true;
                    }
                }
                return false;
            }else{
                if(pointer.contains(value)){
                    pointer = pointer.get(value);
                }else{
                    return false;
                }
            }
        }
        return pointer != null && pointer.isEnd();
    }


    class TrieNode{
        private TrieNode[] nodes = new TrieNode[26];
        private boolean isEnd;

        public boolean contains(char value){
            return get(value) != null;
        }

        public TrieNode get(char value){
            return nodes[value-'a'];
        }

        public void put(char value){
            nodes[value -'a'] = new TrieNode();
        }

        public void setEnd(boolean isEnd){
            this.isEnd = isEnd;
        }

        public boolean isEnd(){
            return isEnd;
        }
    }
}
