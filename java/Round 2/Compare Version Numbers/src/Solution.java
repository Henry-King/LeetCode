import java.math.BigInteger;


public class Solution {
    public int compareVersion(String version1, String version2) {
        String[] v1 = version1.split("\\.");
        String[] v2 = version2.split("\\.");
        BigInteger int1, int2;
        int result, i, min, max;
        min = Math.min(v1.length, v2.length);
        for (i = 0; i < min; i++) {
            int1 = new BigInteger(v1[i]);
            int2 = new BigInteger(v2[i]);
            if ((result = int1.compareTo(int2)) != 0) {
                return result;
            }
        }
        max = Math.max(v1.length, v2.length);
        for(;i<max;i++){
            if(v1.length>v2.length){
                if(!v1[i].matches("0+"))
                    return 1;
            }
            if(v2.length>v1.length){
                if(!v2[i].matches("0+"))
                    return -1;
            }
        }
        return 0;
    }
}