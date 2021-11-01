package com.company;

public class Solution3 {
    public boolean isNumber(String s) {

        // "   44.55e+6   "
        s = s.trim();
        if(s.length() > 0){
            if(s.charAt(0) == '+' || s.charAt(0) == '-'){
                s = s.substring(1);
            }

            // "44.55e+6"
            String execludeIntPart = removeContinuingDigits(s);
            if(execludeIntPart == null){
                if(s.length() == 0 || s.charAt(0) != '.'){
                    return false;
                }
            }else{
                s = execludeIntPart;
            }

            // ".55e+6"
            if(s.length() > 0 && s.charAt(0) == '.'){
                s = s.substring(1);
            }

            // "55e+6"
            String execludeDecimalPart = removeContinuingDigits(s);
            if(execludeIntPart == null && execludeDecimalPart == null){
                return false;
            }

            // "e+6"
            if(execludeDecimalPart!=null){
                s = execludeDecimalPart;
            }

            if(s.length() > 0){
                if(s.charAt(0) != 'e'){
                    return false;
                }
                else{
                    s = s.substring(1);
                }

                // "+6"
                if(s.length() > 0 && (s.charAt(0) == '+' || s.charAt(0) == '-')){
                    s = s.substring(1);
                }

                // "6"
                String execludeExpPart = removeContinuingDigits(s);
                return execludeExpPart != null && execludeExpPart.length() == 0;
            }
        }else{
            return false;
        }

        return true;
    }

    private String removeContinuingDigits(String s){
        int i = 0;
        boolean found = false;
        for(;i<s.length();i++){
            if(s.charAt(i) < '0' || s.charAt(i) > '9'){
                break;
            }else{
                found = true;
            }
        }

        return found ? s.substring(i) : null;
    }
}
