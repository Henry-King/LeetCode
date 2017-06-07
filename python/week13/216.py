class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def helper(temp, k_left, n_left, available_num):
            if n_left == 0 and k_left == 0:
                res.append(temp[:])
            elif k_left != 0 and n_left > 0:
                for k, v in enumerate(available_num):
                    temp.append(v)
                    helper(temp, k_left - 1, n_left - v, available_num[k + 1:] if k + 1 < len(available_num) else [])
                    temp.pop()

        helper([], k, n, range(1, 10))
        return res


s = Solution()
print s.combinationSum3(3, 9)
