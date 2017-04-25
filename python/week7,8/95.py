# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.__helper(n, 1, n, {})

    def __helper(self, n, start, end, cache):
        ret = []
        if end >= start:
            ret.append(TreeNode(start))

            for i in xrange(start + 1, end + 1):
                next_level = []
                for j in xrange(start, i + 1):
                    root = TreeNode(j)

                    if (start, j - 1) in cache:
                        left_branches = cache[(start, j - 1)]
                    else:
                        left_branches = self.__helper(n, start, j - 1, cache)
                        cache[(start, j - 1)] = left_branches

                    if (j + 1, end) in cache:
                        right_branches = cache[(j + 1, end)]
                    else:
                        right_branches = self.__helper(n, j + 1, end, cache)
                        cache[(j + 1, end)] = right_branches

                    if left_branches and right_branches:
                        products = [[x] + [y] for x in left_branches for y in right_branches]
                    elif left_branches and not right_branches:
                        products = [[x] + [None] for x in left_branches]
                    elif not left_branches and right_branches:
                        products = [[None] + [x] for x in right_branches]
                    else:
                        products = []

                    for item in products:
                        root.left = item[0]
                        root.right = item[1]
                        next_level.append(self.__copy_node(root))

                ret = next_level

        return ret

    def __copy_node(self, root):
        ret = None
        if root:
            ret = TreeNode(root.val)
            ret.left = self.__copy_node(root.left)
            ret.right = self.__copy_node(root.right)
        return ret


s = Solution()
r = s.generateTrees(8)
print len(r)
