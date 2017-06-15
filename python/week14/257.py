# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []

        def dfs(node, path):
            path.append(str(node.val))
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
            if not node.left and not node.right:
                result.append("->".join(path))
            path.pop()

        if root:
            dfs(root, [])
        return result
