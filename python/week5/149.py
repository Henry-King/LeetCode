# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        ret = 0
        ks = {}
        for i in xrange(len(points)):
            same_point = 0
            same_x = 1
            ks.clear()
            for j in xrange(len(points)):
                if i != j:
                    if points[i].x == points[j].x and points[i].y == points[j].y:
                        same_point += 1
                    elif points[i].x == points[j].x:
                        same_x += 1
                    else:
                        y = points[i].y - points[j].y
                        x = points[i].x - points[j].x
                        gcd = self.__gcd(y, x)
                        y /= gcd
                        x /= gcd
                        key = (y, x)
                        if key in ks:
                            ks[key] = ks[key] + 1
                        else:
                            ks[key] = 2
                        ret = max(ret, ks[key] + same_point)
            ret = max(ret, same_x + same_point)
        return ret

    def __gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.__gcd(b, a % b)


class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


s = Solution()
print s.maxPoints([Point(0, 0), Point(94911151, 94911150), Point(94911152, 94911151)])
