class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        valid_nums = [1]
        valid_nums.extend([num for num in nums if num > 0])
        valid_nums.append(1)

        mem = [[0] * len(valid_nums) for __ in xrange(len(valid_nums))]

        def burst(left, right):
            if left + 1 == right:
                return 0
            elif mem[left][right] > 0:
                return mem[left][right]
            else:
                res = 0
                for i in xrange(left + 1, right):
                    res = max(res, valid_nums[left] * valid_nums[i] * valid_nums[right] +
                              burst(left, i) + burst(i, right))
                mem[left][right] = res
                return res

        return burst(0, len(valid_nums) - 1)


s = Solution()
print s.maxCoins([3, 1, 5, 8])
