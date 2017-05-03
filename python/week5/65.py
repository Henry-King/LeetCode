class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
        except:
            return False
        else:
            return True


s = Solution()
print s.isNumber("1 a")
