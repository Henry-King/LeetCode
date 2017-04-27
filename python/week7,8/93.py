class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        if s:
            self.__helper(s, 0, [], ret)
        return ret

    def __helper(self, s, index, temp, ret):
        if len(temp) == 4:
            if index == len(s):
                ret.append(".".join(temp))
        elif len(temp) < 4:
            for i in xrange(index, index + 3 if index + 3 <= len(s) else len(s)):
                item = s[index:i + 1]
                if (item[0] != '0' or (item[0] == '0' and len(item) == 1)) and int(item) <= 255:
                    temp.append(item)
                    self.__helper(s, i + 1, temp, ret)
                    temp.pop()


s = Solution()
print s.restoreIpAddresses("0000")
