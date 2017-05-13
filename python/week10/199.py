# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root:
            cur_level = deque()
            cur_level.append(root)
            while cur_level:
                next_level = deque()
                while cur_level:
                    node = cur_level.popleft()
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                    if not cur_level:
                        ret.append(node.val)
                cur_level = next_level
        return ret


a = TreeNode(1)
a.left = TreeNode(2)
s = Solution()
print s.rightSideView(a)
