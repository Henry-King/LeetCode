class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ret = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while carry or i >= 0 or j >= 0:
            foo, bar = 0, 0
            if i >= 0:
                foo = int(a[i])
                i -= 1
            if j >= 0:
                bar = int(b[j])
                j -= 1
            carry, remainder = divmod(foo + bar + carry, 2)
            ret.append(str(remainder))
        ret.reverse()
        return "".join(ret)


s = Solution()
print s.addBinary("11", "1")
