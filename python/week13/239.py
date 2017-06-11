from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        if nums and k > 0:
            q = deque()
            for i, v in enumerate(nums):
                while q and q[0] < i - k + 1:
                    q.popleft()
                while q and nums[q[-1]] < v:
                    q.pop()

                q.append(i)
                if i >= k - 1:
                    res.append(nums[q[0]])
        return res


s = Solution()
print s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
