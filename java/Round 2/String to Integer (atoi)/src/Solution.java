public class Solution {
    public int myAtoi(String str) {
        boolean positive = true, overFlow = false, start = false;
        long value = 0;
        char[] chars = str.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == ' ') {
                if (start)
                    break;
            } else if (chars[i] == '+') {
                if (start) {
                    value = 0;
                    break;
                } else {
                    positive = true;
                    start = true;
                }
            } else if (chars[i] == '-') {
                if (start) {
                    value = 0;
                    break;
                } else {
                    positive = false;
                    start = true;
                }
            } else if (chars[i] >= '0' && chars[i] <= '9') {
                start = true;
                if (positive)
                    value = value * 10 + chars[i] - '0';
                else
                    value = value * 10 - (chars[i] - '0');
                if ((positive && value <= Integer.MAX_VALUE) || (!positive && value >= Integer.MIN_VALUE))
                    ;
                else {
                    overFlow = true;
                    break;
                }
            } else {
                break;
            }
        }
        if (!start)
            return 0;
        else {
            if (overFlow)
                return positive ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            else {
                return (int)value;
            }
        }
    }
}