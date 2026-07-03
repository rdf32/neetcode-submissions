class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        for ind in range(len(heights)):
            dist = 1
            left, right = ind - 1, ind + 1
            while left >= 0:
                if heights[left] >= heights[ind]:
                    dist += 1
                    left -= 1
                else:
                    break
            while right < len(heights):
                if heights[right] >= heights[ind]:
                    dist += 1
                    right += 1
                else:
                    break
            max_area = max(max_area, dist * heights[ind])

        return max_area