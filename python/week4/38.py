class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = ["1"]

        for i in xrange(1, n):
            temp = []
            pointer = 0
            length = len(ret)
            for j in xrange(len(ret)):
                if ret[j] != ret[pointer]:
                    temp.extend([str(j - pointer), str(ret[pointer])])
                    pointer = j
            temp.extend([str(length - pointer), str(ret[pointer])])
            ret = temp
        return "".join(ret)


s = Solution()
print s.countAndSay(5)
