class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in xrange(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row


s = Solution()
print s.getRow(3)
