class SegmentTree(object):
    pass


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        def __build_tree(nums, start, end):
            if start <= end:
                root = SegmentTree()
                root.start = start
                root.end = end
                if start == end:
                    root.sum = nums[start]
                else:
                    mid = (start + end) / 2
                    root.left = __build_tree(nums, start, mid)
                    root.right = __build_tree(nums, mid + 1, end)
                    root.sum = root.left.sum + root.right.sum
                return root

        self.root = __build_tree(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """

        def __update(root, i, val):
            if root.start == root.end:
                root.sum = val
            else:
                mid = (root.start + root.end) / 2
                if i <= mid:
                    __update(root.left, i, val)
                else:
                    __update(root.right, i, val)
                root.sum = root.left.sum + root.right.sum

        __update(self.root, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        def __sum_tree(node, start, end):
            if node.start == start and node.end == end:
                return node.sum
            else:
                mid = (node.start + node.end) / 2
                if mid >= end:
                    return __sum_tree(node.left, start, end)
                elif mid + 1 <= start:
                    return __sum_tree(node.right, start, end)
                else:
                    return __sum_tree(node.left, start, mid) + __sum_tree(node.right, mid + 1, end)

        return __sum_tree(self.root, i, j)

        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # obj.update(i,val)
        # param_2 = obj.sumRange(i,j)


s = NumArray([1, 3, 5])
print s.sumRange(0, 2)
s.update(1, 2)
print s.sumRange(0, 2)
