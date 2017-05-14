# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sums = 0
        if root:
            cur_level = deque()
            cur_level.append(root)
            while cur_level:
                next_level = deque()
                while cur_level:
                    node = cur_level.popleft()
                    if node.left:
                        node.left.val += node.val * 10
                        next_level.append(node.left)
                    if node.right:
                        node.right.val += node.val * 10
                        next_level.append(node.right)
                    if not node.left and not node.right:
                        sums += node.val
                cur_level = next_level
        return sums
