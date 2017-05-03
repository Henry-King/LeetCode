class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums:
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right) / 2
                if nums[mid] == target:
                    left = mid
                    break
                else:
                    if nums[mid] >= nums[left]:
                        if nums[mid] > target >= nums[left]:
                            right = mid - 1
                        else:
                            left = mid + 1
                    else:
                        if nums[mid] < target <= nums[right]:
                            left = mid + 1
                        else:
                            right = mid - 1
            if nums[left] == target:
                return left
        return -1


s = Solution()
print s.search([3, 5, 1], 1)
