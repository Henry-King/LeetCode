# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        ret = n
        while lo < hi:
            mid = (lo + hi) / 2
            if isBadVersion(mid):
                ret = mid
                if hi == mid:
                    break
                else:
                    hi = mid
            else:
                if lo == mid:
                    break
                else:
                    lo = mid
        return ret
