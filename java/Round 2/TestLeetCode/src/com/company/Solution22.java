package com.company;

public class Solution22 {
    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        } else {
            boolean positive = (dividend > 0 && divisor > 0) || (dividend < 0 && divisor < 0);
            dividend = dividend > 0 ? -dividend : dividend;
            divisor = divisor > 0 ? -divisor : divisor;
            int quotient = 0;

            while (dividend <= divisor) {
                int powerOfTwo = 1, value = divisor;
                while (value + value > dividend && value + value <0) {
                    powerOfTwo += powerOfTwo;
                    value += value;
                }

                quotient += powerOfTwo;
                dividend -= value;
            }

            return positive ? quotient : -quotient;
        }
    }
}
