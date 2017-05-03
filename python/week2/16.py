class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        targets = list(set(nums))
        nums.sort()
        targets.sort()
        closet = nums[0] + nums[1] + nums[2]
        for item in targets:
            sub_nums = nums[nums.index(item):]
            sub_nums.remove(item)
            if len(sub_nums) >= 2:
                ret = self.__two_sum(sub_nums, target - item)
                if abs(target - ret - item) < abs(target - closet):
                    closet = ret + item
            else:
                break
        return closet

    def __two_sum(self, nums, target):
        left = 0
        right = len(nums) - 1
        closet = nums[left] + nums[right]
        while left < right:
            two_sum = nums[left] + nums[right]
            if abs(target - two_sum) < abs(target - closet):
                closet = two_sum
            if two_sum < target:
                left += 1
            elif two_sum > target:
                right -= 1
            else:
                break
        return closet


s = Solution()
print s.threeSumClosest([0, 1, 2], 1)
