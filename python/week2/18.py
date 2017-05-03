class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        return Solution.__n_sum(nums, target, self.__three_sum)

    def __three_sum(self, nums, target):
        return Solution.__n_sum(nums, target, Solution.__two_sum)

    @staticmethod
    def __two_sum(nums, target):
        ret = []
        if len(nums) >= 2:
            left = 0
            right = len(nums) - 1
            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    ret.append([nums[left], nums[right]])
                    pre_left = left
                    while left < right and nums[pre_left] == nums[left]:
                        left += 1
                    pre_right = right
                    while left < right and nums[pre_right] == nums[right]:
                        right -= 1

        return ret

    @staticmethod
    def __n_sum(nums, target, sub_sum_function):
        ret = []
        remove_duplicate = list(set(nums))
        remove_duplicate.sort()
        for searched_key in remove_duplicate:
            key_index = nums.index(searched_key)
            target_list = nums[key_index+1:] if key_index < len(nums) else nums[key_index:]

            sub_sum_list = sub_sum_function(target_list[:], target - searched_key)

            if sub_sum_list:
                for item in sub_sum_list:
                    item.append(searched_key)
                ret.extend(sub_sum_list)
        return ret

s = Solution()
print s.fourSum([1, 0, -1, 0, -2, 2], 0)
