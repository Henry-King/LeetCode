class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        bucket = [0 for i in xrange(len(citations) + 1)]
        for index, value in enumerate(citations):
            if value >= len(citations):
                bucket[len(citations)] += 1
            else:
                bucket[value] += 1

        count = 0
        for index, value in reversed(list(enumerate(bucket))):
            count += value
            if count >= index:
                return index
        return 0


s = Solution()
print s.hIndex([1, 1])
