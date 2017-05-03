class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        duplicate_index = -1
        search_index = 0

        while search_index - duplicate_index <= length:
            if nums[search_index] == val:
                nums[duplicate_index], nums[search_index] = nums[search_index], nums[duplicate_index]
                duplicate_index -= 1
            else:
                search_index += 1

        return search_index


x = [3, 2, 2, 3]
s = Solution()
print s.removeElement(x, 3)
print x

