class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        for num in nums:
            temp = []
            for possible in ret:
                for position in xrange(len(possible) + 1):
                    temp.append(possible[:position] + [num] + possible[position:])
                    if position < len(possible) and num == possible[position]:
                        break
            ret = temp
        return ret


s = Solution()
print s.permuteUnique([1, 1, 2])
