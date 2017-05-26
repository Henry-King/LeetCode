class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle:
            pre = [0]
            for row in triangle:
                cur = row[:]
                for index in xrange(len(cur)):
                    if index == 0:
                        cur[index] += pre[index]
                    elif index == len(cur) - 1:
                        cur[index] += pre[index - 1]
                    else:
                        cur[index] += min(pre[index - 1], pre[index])
                pre = cur
            return min(pre)
        else:
            return 0


s = Solution()
print s.minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
])
