class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        targets = list(set(nums))
        nums.sort()
        targets.sort()
        for target in targets:
            sub_list = nums[nums.index(target):]
            sub_list.remove(target)
            ret.extend(self.__twoSum(-target, sub_list))
        return ret

    def __twoSum(self, target, nums):
        ret = []
        if len(nums) >= 2:
            left = 0
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    ret.append(sorted([nums[left], nums[right], -target]))
                    pre_left = left
                    pre_right = right
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[pre_left]:
                        left += 1
                    while right > left and nums[right] == nums[pre_right]:
                        right -= 1
        return ret


s = Solution()
print s.threeSum([-2, 0, 1, 1, 2])
