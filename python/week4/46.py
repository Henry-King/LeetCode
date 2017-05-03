class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        for num in nums:
            temp = []
            for answer in ret:
                for i in xrange(len(answer) + 1):
                    temp.append(answer[:i] + [num] + answer[i:])
            ret = temp
        return ret


s = Solution()
print s.permute([1, 2, 3])
