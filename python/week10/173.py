# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.levels = []
        self.__appendTree(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.levels) > 0

    def next(self):
        """
        :rtype: int
        """
        node = self.levels.pop()
        if node.right:
            self.__appendTree(node.right)
        return node.val

    def __appendTree(self, root):
        while root:
            self.levels.append(root)
            root = root.left
            # Your BSTIterator will be called like this:
            # i, v = BSTIterator(root), []
            # while i.hasNext(): v.append(i.next())
