public class Solution {
    public String reverseWords(String s) {
        char[] chars=s.toCharArray();
        StringBuilder builder = new StringBuilder();
        StringBuilder word =new StringBuilder();
        for(int i=0;i<chars.length;i++){
            if(chars[i]==' ') {
                if(word.length()!=0) {
                    builder.insert(0, word);
                    builder.insert(0,' ');
                    word.setLength(0);
                }
            }
            else{
                word.append(chars[i]);
            }
        }
        if(word.length()!=0)
            builder.insert(0,word);
        if(builder.length()!=0&&builder.charAt(0)==' ')
            builder.deleteCharAt(0);
        return builder.toString();
    }
}