# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left, right = [], []
        start, end = newInterval.start, newInterval.end
        for item in intervals:
            if item.end < start:
                left.append(item)
            elif item.start > end:
                right.append(item)
            else:
                start = min(start, item.start)
                end = max(item.end, end)
        return left + [Interval(start, end)] + right


s = Solution()
a = Interval(1, 5)
i = Interval(6, 8)
s.insert([a], i)
