class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) / 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    first_occur_left = left
                    first_occur_right = mid
                    first_occur = mid
                    while first_occur_left <= first_occur_right:
                        first_occur_mid = (first_occur_left + first_occur_right) / 2
                        if nums[first_occur_mid] != target:
                            first_occur_left = first_occur_mid + 1
                        else:
                            first_occur = first_occur_mid
                            first_occur_right = first_occur_mid - 1

                    last_occur_left = mid
                    last_occur_right = right
                    last_occur = mid
                    while last_occur_left <= last_occur_right:
                        last_occur_mid = (last_occur_left + last_occur_right) / 2
                        if nums[last_occur_mid] != target:
                            last_occur_right = last_occur_mid - 1
                        else:
                            last_occur = last_occur_mid
                            last_occur_left = last_occur_mid + 1
                    return [first_occur, last_occur]
        return [-1, -1]


s = Solution()
print s.searchRange([2,2], 2)
