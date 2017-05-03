import sys


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        nums1_len = len(nums1)
        nums2_len = len(nums2)

        if nums2_len == 0:
            return (nums1[(nums1_len - 1) / 2] + nums1[nums1_len / 2]) / 2.0
        else:
            left_bound = 0
            right_bound = nums2_len * 2 + 1

            while left_bound <= right_bound:
                c2 = (left_bound + right_bound) / 2
                c1 = nums1_len + nums2_len - c2

                l1 = -sys.maxint - 1 if c1 == 0 else nums1[(c1 - 1) / 2] * 1.0
                r1 = sys.maxint if c1 == 2 * nums1_len else nums1[c1 / 2] * 1.0
                l2 = -sys.maxint - 1 if c2 == 0 else nums2[(c2 - 1) / 2] * 1.0
                r2 = sys.maxint if c2 == 2 * nums2_len else nums2[c2 / 2] * 1.0

                if l1 <= r2 and l2 <= r1:
                    return (max(l1, l2) + min(r1, r2)) / 2
                elif l1 > r2:
                    left_bound = c2 + 1
                else:
                    right_bound = c2 - 1


s = Solution()
print s.findMedianSortedArrays([100000], [100001])
