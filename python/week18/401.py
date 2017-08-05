from itertools import combinations


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ret = []
        for i in xrange(num + 1):
            ret.extend([a + ':' + b for a in self.hours(i) for b in self.minutes(num - i)])
        return ret

    def hours(self, on):
        return [str(item) for item in filter(lambda value: value < 12, map(sum, combinations([1, 2, 4, 8], on)))]

    def minutes(self, on):
        return [str(item).rjust(2, '0') for item in
                filter(lambda value: value < 60, map(sum, combinations([1, 2, 4, 8, 16, 32], on)))]


s = Solution()
print s.readBinaryWatch(2)
