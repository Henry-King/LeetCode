class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        lo, hi = 0, len(citations) - 1
        while lo <= hi:
            mid = (lo + hi) >> 1
            if citations[mid] == len(citations) - mid:
                return citations[mid]
            elif citations[mid] > len(citations) - mid:
                hi = mid - 1
            else:
                lo = mid + 1
        return len(citations) - (hi + 1)


s = Solution()
print s.hIndex([0, 0])
