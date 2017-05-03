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
        if n > 0:
            return self.__helper(n, 1, n, {})
        else:
            return []

    def __helper(self, n, start, end, cache):
        ret = []
        if end == start:
            ret.append(TreeNode(start))
        elif start > end:
            ret.append(None)
        else:
            for j in xrange(start, end + 1):
                left_branches = self.__fetch_from_catch(cache, start, j - 1, n)
                right_branches = self.__fetch_from_catch(cache, j + 1, end, n)
                products = [[x] + [y] for x in left_branches for y in right_branches]

                for item in products:
                    root = TreeNode(j)
                    root.left = item[0]
                    root.right = item[1]
                    ret.append(root)
        return ret

    def __fetch_from_catch(self, cache, start, end, n):
        key = (start, end)
        if key in cache:
            branches = cache[key]
        else:
            branches = self.__helper(n, start, end, cache)
            cache[key] = branches
        return branches


s = Solution()
r = s.generateTrees(3)
print len(r)
