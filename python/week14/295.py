from Queue import PriorityQueue


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.large = PriorityQueue()
        self.small = PriorityQueue()

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.large.put_nowait(num)
        self.small.put_nowait(-self.large.get_nowait())
        if self.large.qsize() < self.small.qsize():
            self.large.put_nowait(-self.small.get_nowait())

    def findMedian(self):
        """
        :rtype: float
        """
        return self.large.queue[0] if self.large.qsize() > self.small.qsize() else \
            (self.large.queue[0] - self.small.queue[0]) / 2.0


        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()


s = MedianFinder()
s.addNum(1)
s.addNum(2)
print s.findMedian()
s.addNum(3)
print s.findMedian()
