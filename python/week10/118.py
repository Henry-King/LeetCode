class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        if numRows > 0:
            ret.append([1])
            if numRows > 1:
                for j in xrange(1, numRows):
                    prev = ret[j - 1]
                    cur = [prev[index] + prev[index - 1] if 0 < index < len(prev) else 1 for index in
                           xrange(len(prev) + 1)]
                    ret.append(cur)
        return ret


s = Solution()
print s.generate(5)
