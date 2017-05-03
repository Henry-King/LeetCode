# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.__helper(root, None, None)

    def __helper(self, root, min_key, max_key):
        if root:
            if (max_key is not None and root.val >= max_key) or (min_key is not None and root.val <= min_key):
                return False
            else:
                return self.__helper(root.left, min_key, root.val) and self.__helper(root.right, root.val, max_key)
        else:
            return True
