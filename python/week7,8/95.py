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
                    left_branches = self.__fetch_from_catch(cache, start, j - 1, n)
                    right_branches = self.__fetch_from_catch(cache, j + 1, end, n)

                    left_branches = [[]] if left_branches == [] else left_branches
                    right_branches = [[]] if right_branches == [] else right_branches
                    products = [[x] + [y] for x in left_branches for y in right_branches]

                    if left_branches != [[]] or right_branches != [[]]:
                        for item in products:
                            root.left = item[0]
                            root.right = item[1]
                            next_level.append(self.__copy_node(root))

                ret = next_level
        return ret

    def __fetch_from_catch(self, cache, start, end, n):
        key = (start, end)
        if key in cache:
            branches = cache[key]
        else:
            branches = self.__helper(n, start, end, cache)
            cache[key] = branches
        return branches

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
