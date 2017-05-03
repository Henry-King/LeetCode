class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = list(s)
        left = 0
        right = len(str_list) - 1
        while left < right:
            str_list[left], str_list[right] = str_list[right], str_list[left]
            left += 1
            right -= 1
        return "".join(str_list)

s = Solution()
print s.reverseString("hello")
