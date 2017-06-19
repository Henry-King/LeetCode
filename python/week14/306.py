class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        def is_valid(foo, bar, num):
            if num:
                foo, bar = bar, foo + bar
                return num.startswith(str(bar)) and is_valid(foo, bar, num[len(str(bar)):])
            else:
                return True

        for i in xrange(1, len(num) / 2 + 1):
            if num[0] == '0' and i > 1:
                return False
            else:
                for j in xrange(1, len(num)):
                    if max(i, j) <= len(num) - (i + j) and not (num[i] == '0' and j > 1):
                        first = int(num[:i])
                        second = int(num[i:i + j])
                        if is_valid(first, second, num[i + j:]):
                            return True
                    else:
                        break
        return False


s = Solution()
print s.isAdditiveNumber("199100199")
