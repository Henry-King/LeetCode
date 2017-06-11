class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        buckets = {}
        for i, v in enumerate(nums):
            bucket_index, offset = (v / t, 1) if t else (v, 0)
            for index in xrange(bucket_index - offset, bucket_index + offset + 1):
                if index in buckets and abs(v - buckets[index]) <= t:
                    return True

            buckets[bucket_index] = v

            if len(buckets) > k:
                del buckets[nums[i - k] / t if t else nums[i - k]]
        return False
