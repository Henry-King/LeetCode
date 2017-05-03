class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left = 0
        right = len(height) - 1
        left_max_height = 0
        right_max_height = 0
        while left < right:
            left_max_height = max(left_max_height, height[left])
            right_max_height = max(right_max_height, height[right])
            if left_max_height < right_max_height:
                area += left_max_height - height[left]
                left += 1
            else:
                area += right_max_height - height[right]
                right -= 1
        return area


s = Solution()
print s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
