import random


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.__findKthLargest(nums, 0, len(nums)-1, k)

    def __findKthLargest(self, nums, start, end, kthLarget):
        if end == start:
            return nums[start]
        else:
            pivot = self.__random_partition(nums, start, end)
            pivot_order = end - pivot + 1
            if pivot_order == kthLarget:
                return nums[pivot]
            elif pivot_order > kthLarget:
                return self.__findKthLargest(nums, pivot + 1, end, kthLarget)
            else:
                return self.__findKthLargest(nums, start, pivot - 1, kthLarget - pivot_order)

    def __random_partition(self, nums, start, end):
        select_index = random.randrange(start, end)
        self.__swap(nums, select_index, end)
        return self.__partition(nums, start, end)

    def __partition(self, nums, start, end):
        pivot = nums[end]
        pivot_index = start - 1
        for i in range(start, end+1):
            value = nums[i]
            if value < pivot:
                pivot_index += 1
                self.__swap(nums, i, pivot_index)
        self.__swap(nums, pivot_index + 1, end)
        return pivot_index + 1

    def __swap(self, nums, foo, bar):
        temp = nums[foo]
        nums[foo] = nums[bar]
        nums[bar] = temp


s = Solution()
print s.findKthLargest([3, 2, 1, 5, 6, 4], 2)
