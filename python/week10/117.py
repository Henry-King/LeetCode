# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


from collections import deque


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
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
                    if cur_level:
                        node.next = cur_level[0]
                cur_level = next_level
