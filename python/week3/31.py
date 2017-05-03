class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums and len(nums) > 1:
            num_length = len(nums)
            out_order_index = num_length - 2
            while out_order_index >= 0:
                if nums[out_order_index] < nums[out_order_index + 1]:
                    break
                out_order_index -= 1

            if out_order_index >= 0:
                min_larger_index = out_order_index + 1
                while min_larger_index < num_length and nums[min_larger_index] > nums[out_order_index]:
                    min_larger_index += 1

                min_larger_index -= 1
                nums[min_larger_index], nums[out_order_index] = nums[out_order_index], nums[min_larger_index]

            i = out_order_index + 1
            j = num_length - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1


s = Solution()
x = [3, 2, 1]
s.nextPermutation(x)
print x
