class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        word_size, ending_offset = 1, 1
        multiplier = 9
        while n > multiplier * word_size:
            n -= multiplier * word_size
            word_size += 1
            multiplier *= 10
            ending_offset *= 10

        offset = divmod((n - 1), word_size)
        return int(str(ending_offset + offset[0])[offset[1]])


s = Solution()
print s.findNthDigit(11)
