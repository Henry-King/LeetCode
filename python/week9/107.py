from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        cur_level = deque()
        if root:
            cur_level.append(root)

        while cur_level:
            level_ret = []
            for i in range(len(cur_level)):
                node = cur_level.popleft()
                if node.left:
                    cur_level.append(node.left)
                if node.right:
                    cur_level.append(node.right)
                level_ret.append(node.val)
            ret.append(level_ret)
        ret.reverse()
        return ret
