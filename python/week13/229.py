class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums:
            count1, num1, count2, num2 = 0, None, 0, None
            for num in nums:
                if num == num1:
                    count1 += 1
                elif num == num2:
                    count2 += 1
                elif count1 == 0:
                    num1, count1 = num, 1
                elif count2 == 0:
                    num2, count2 = num, 1
                else:
                    count1 -= 1
                    count2 -= 1
            return [num for num in [num1, num2] if nums.count(num) > len(nums) / 3]
        else:
            return []


s = Solution()
print s.majorityElement([2, 2])
