class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(len(heights)):
            area = heights[i]
            if area > 0:
                left, right = i - 1, i + 1
                while left >= 0 and heights[left] >= heights[i]:
                    area += heights[i]
                    left -= 1
                
                while right < len(heights) and heights[right] >= heights[i]:
                    area += heights[i]
                    right += 1
            maxArea = max(maxArea, area)
        
        return maxArea