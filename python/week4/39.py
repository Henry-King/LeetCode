class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ret = []
        temp = []
        self.__find_sum(candidates, target, ret, temp)
        return ret

    def __find_sum(self, candidates, target, result, temp):
        if target < 0:
            return
        elif target == 0:
            result.append(temp[:])
        else:
            if candidates and target >= candidates[0]:
                for index, value in enumerate(candidates):
                    temp.append(value)
                    self.__find_sum(candidates[index:], target - value, result, temp)
                    temp.pop()


s = Solution()
print s.combinationSum([2, 3, 6, 7], 7)
