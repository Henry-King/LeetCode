class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums:
            lo = 0
            hi = len(nums) - 1
            while lo < hi:
                mid = (lo + hi) / 2
                if nums[mid] == target:
                    return True
                else:
                    if nums[mid] > nums[lo]:
                        if nums[lo] <= target < nums[mid]:
                            hi = mid - 1
                        else:
                            lo = mid + 1
                    elif nums[mid] < nums[lo]:
                        if nums[mid] < target <= nums[hi]:
                            lo = mid + 1
                        else:
                            hi = mid - 1
                    else:
                        lo += 1
            return True if nums[lo] == target else False

        else:
            return False


s = Solution()
print s.search([1, 3, 1, 1, 1], 3)
