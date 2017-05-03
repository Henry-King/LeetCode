class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) / 2
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    return mid

            return left

        else:
            return 0


s = Solution()
print s.searchInsert([1, 3, 5, 6], 0)
