class Solution(object):
    sub_notation = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }

    normal_notation = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in Solution.sub_notation:
                ret += Solution.sub_notation[s[i:i+2]]
                i += 1
            else:
                ret += Solution.normal_notation[s[i]]
            i += 1
        return ret

s = Solution()
print s.romanToInt("MCMXCVI")
