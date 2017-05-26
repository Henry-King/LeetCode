# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ret = []
        self.__helper(root, sum, [], ret)
        return ret

    def __helper(self, root, sum, cur, ret):
        if root:
            cur.append(root.val)
            if not root.left and not root.right:
                if sum == root.val:
                    ret.append(cur[:])
            else:
                self.__helper(root.left, sum - root.val, cur, ret)
                self.__helper(root.right, sum - root.val, cur, ret)
            cur.pop()
