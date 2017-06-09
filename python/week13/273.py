from collections import deque


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        else:
            less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                            "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            thousand = ["", "Thousand", "Million", "Billion"]

            def less_than_thousand(digit):
                if digit == 0:
                    return ""
                elif digit < 20:
                    return "".join((less_than_20[digit], " "))
                elif digit < 100:
                    return "".join((tens[digit / 10], " ", less_than_thousand(digit % 10)))
                else:
                    return "".join((less_than_20[digit / 100], " Hundred ", less_than_thousand(digit % 100)))

            count = 0
            res = deque()
            while num:
                if num % 1000:
                    res.appendleft(" ")
                    res.appendleft(thousand[count])
                    res.appendleft(less_than_thousand(num % 1000))
                count += 1
                num /= 1000
            return "".join(res).strip()


s = Solution()
print s.numberToWords(1234567)
