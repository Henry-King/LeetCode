from collections import deque


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]l
        """
        intervals = sorted(intervals, key=lambda interval: interval.start)
        intervals = deque(intervals)
        ret = []

        while len(intervals) > 1:
            if intervals[0].end >= intervals[1].start:
                intervals[1].start = intervals[0].start
                if intervals[0].end > intervals[1].end:
                    intervals[1].end = intervals[0].end
            else:
                ret.append(intervals[0])
            intervals.popleft()

        if len(intervals) == 1:
            ret.append(intervals[0])
        return ret


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


s = Solution()
a = Interval(1, 4)
b = Interval(2, 3)
print s.merge([a, b])
