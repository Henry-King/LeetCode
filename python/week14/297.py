# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def preorder(node):
            if node:
                res.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                res.append('X')

        preorder(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = deque(data.split(','))

        def toTree():
            node = queue.popleft()
            if node == 'X':
                return None
            else:
                root = TreeNode(int(node))
                root.left = toTree()
                root.right = toTree()
                return root

        return toTree()


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))


r = TreeNode(0)
r.left = TreeNode(0)
r.right = TreeNode(0)
r.left.left = TreeNode(0)
r.right.right = TreeNode(1)

s = Codec()
res = s.serialize(None)
s.deserialize(res)
