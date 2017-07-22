from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        bucket = defaultdict(int)
        freq_bucket = [set() for __ in xrange(len(nums)+1)]
        ret = []
        for i in nums:
            bucket[i] += 1

        for item, freq in bucket.items():
            freq_bucket[freq].add(item)

        for item in reversed(freq_bucket):
            if len(ret) < k:
                if item:
                    ret.extend(item)
            else:
                break

        return ret


s = Solution()
print s.topKFrequent([1], 1)
