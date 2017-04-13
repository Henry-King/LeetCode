class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        max_area = i = 0
        while i <= len(heights):
            cur = heights[i] if i < len(heights) else 0
            if not stack or cur >= heights[stack[len(stack) - 1]]:
                stack.append(i)
                i += 1
            else:
                top = heights[stack.pop()]
                width = (i - stack[len(stack) - 1] - 1) if stack else i
                max_area = max(max_area, top * width)
        return max_area


s = Solution()
print s.largestRectangleArea([2, 1, 5, 6, 2, 3])
