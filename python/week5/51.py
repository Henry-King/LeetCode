class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        counts = []
        ret = []

        def dfs(queens, xy_sum, xy_diff):
            row_count = len(queens)
            if row_count == n:
                counts.append(queens.copy())
            else:
                for column in xrange(n):
                    if column not in queens and column + row_count not in xy_sum and row_count - column not in xy_diff:
                        queens[column] = row_count
                        xy_sum.add(row_count + column)
                        xy_diff.add(row_count - column)
                        dfs(queens, xy_sum, xy_diff)
                        del queens[column]
                        xy_sum.remove(row_count + column)
                        xy_diff.remove(row_count - column)

        dfs({}, set(), set())

        for item in counts:
            temp = [i for i in xrange(n)]
            for k, v in item.items():
                temp[v] = k
            ret.append(temp)

        return [['.' * j + 'Q' + '.' * (n - j - 1) for j in i] for i in ret]


s = Solution()
print s.solveNQueens(4)
