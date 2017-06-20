class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if edges:
            adj = [set() for __ in xrange(n)]
            for i, j in edges:
                adj[i].add(j)
                adj[j].add(i)

            leaves = [i for i in xrange(n) if len(adj[i]) == 1]

            while n > 2:
                n -= len(leaves)
                new_leaves = []
                for leaf in leaves:
                    j = adj[leaf].pop()
                    adj[j].remove(leaf)
                    if len(adj[j]) == 1:
                        new_leaves.append(j)
                leaves = new_leaves
            return leaves
        else:
            return [0]


s = Solution()
print s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
