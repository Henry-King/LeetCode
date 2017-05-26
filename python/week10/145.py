# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def helper(node, ret):
            if node:
                helper(node.left, ret)
                helper(node.right, ret)
                ret.append(node.val)
            return ret

        return helper(root, [])


a = TreeNode(1)
a.left = TreeNode(2)
s = Solution()
print s.postorderTraversal(a)
