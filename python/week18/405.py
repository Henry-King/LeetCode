class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = []
        negative = False
        if num < 0:
            num += 2 ** 32
            negative = True

        if num == 0 and not negative:
            ret.append('0')
        else:
            while num > 0:
                num, remainder = divmod(num, 16)
                if remainder < 10:
                    ret.append(str(remainder))
                else:
                    ret.append(chr(ord('a') + remainder - 10))

        if negative:
            if len(ret) < 8:
                ret.extend(['0'] * (7 - len(ret)))
                ret.append('f')

        ret.reverse()
        return "".join(ret)


s = Solution()
print s.toHex(-1)
