class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret_set = set(nums1).intersection(set(nums2))
        ret = []
        for item in ret_set:
            for count in range(min(nums1.count(item), nums2.count(item))):
                ret.append(item)
        return ret


s = Solution()
print s.intersect([1, 2, 2, 1], [2, 2])
