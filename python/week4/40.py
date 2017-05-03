class Solution(object):
    def combinationSum2(self, candidates, target):
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
                    if index > 0 and candidates[index] == candidates[index - 1]:
                        continue
                    else:
                        temp.append(value)
                        self.__find_sum(candidates[index + 1:], target - value, result, temp)
                        temp.pop()


s = Solution()
print s.combinationSum2(
    [14, 6, 25, 9, 30, 20, 33, 34, 28, 30, 16, 12, 31, 9, 9, 12, 34, 16, 25, 32, 8, 7, 30, 12, 33, 20, 21, 29, 24, 17,
     27, 34, 11, 17, 30, 6, 32, 21, 27, 17, 16, 8, 24, 12, 12, 28, 11, 33, 10, 32, 22, 13, 34, 18, 12]
    , 27)
