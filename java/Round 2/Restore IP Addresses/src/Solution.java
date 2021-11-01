/**
 * Created by sy on 15/9/24.
 */
public class Solution {
    private final static int DIGIT_NUM = 3;
    private final static int DOT_NUM = 3;
    private final static int ITEM_RANGE = 256;
    private final static int DEC = 10;

    public Integer toIPAddress(String ipAddress) {
        boolean success = true;
        char item;
        int dotNum = 0, itemNum = 0, decimal = 0, result = 0;
        for (int i = 0; i < ipAddress.length(); i++) {
            item = ipAddress.charAt(i);
            if (isDigit(item)) {
                if (itemNum < DIGIT_NUM) {
                    decimal = decimal * DEC + item - '0';
                    itemNum++;
                } else {
                    success = false;
                    break;
                }
            } else if (item == '.') {
                if (dotNum < DOT_NUM && decimal < ITEM_RANGE) {
                    result <<= 8;
                    result += decimal;
                    dotNum++;
                    itemNum = 0;
                    decimal = 0;
                } else {
                    success = false;
                    break;
                }
            } else {
                success = false;
                break;
            }
        }
        if (dotNum == DOT_NUM && success) {
            result <<= 8;
            result += decimal;
            return result;
        } else
            return null;
    }

    private boolean isDigit(char item) {
        return item >= '0' && item <= '9';
    }
}
