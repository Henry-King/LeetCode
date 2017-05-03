from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        cur_level = deque()
        if root:
            cur_level.append(root)

        while cur_level:
            cur_level_ret = []
            ltr = (len(ret) % 2 == 0)

            for i in range(len(cur_level)):
                cur_node = cur_level.popleft()
                if cur_node.left:
                    cur_level.append(cur_node.left)
                if cur_node.right:
                    cur_level.append(cur_node.right)
                cur_level_ret.append(cur_node.val)

            if not ltr:
                cur_level_ret.reverse()
            ret.append(cur_level_ret)

        return ret
