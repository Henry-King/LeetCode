from collections import deque


# Definition
# for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        cur_level = deque()
        if root:
            cur_level.append(root)

        while cur_level:
            next_level = deque()
            cur_level_ret = []

            while cur_level:
                node = cur_level.popleft()
                cur_level_ret.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            ret.append(cur_level_ret)
            cur_level = next_level

        return ret
