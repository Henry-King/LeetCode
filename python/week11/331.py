class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        degree = 1
        for item in nodes:
            degree -= 1
            if degree < 0:
                return False
            elif item != '#':
                degree += 2
        return degree == 0


s = Solution()
print s.isValidSerialization("9,#,#,1")
