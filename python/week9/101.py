# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.__helper(root.left, root.right)
        else:
            return True

    def __helper(self, foo, bar):
        if foo and bar:
            if foo.val == bar.val:
                return self.__helper(foo.left, bar.right) and self.__helper(foo.right, bar.left)
            else:
                return False
        elif not foo and not bar:
            return True
        else:
            return False
