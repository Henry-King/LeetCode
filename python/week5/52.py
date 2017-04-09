class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0]

        def dfs(queens, xy_sum, xy_diff):
            row_count = len(queens)
            if row_count == n:
                count[0] = count[0] + 1
            else:
                for column in xrange(n):
                    sums = row_count + column
                    diffs = row_count - column
                    if column not in queens and sums not in xy_sum and diffs not in xy_diff:
                        queens[column] = row_count
                        xy_sum.add(sums)
                        xy_diff.add(diffs)
                        dfs(queens, xy_sum, xy_diff)
                        del queens[column]
                        xy_sum.remove(sums)
                        xy_diff.remove(diffs)

        dfs({}, set(), set())
        return count[0]


s = Solution()
print s.totalNQueens(4)
