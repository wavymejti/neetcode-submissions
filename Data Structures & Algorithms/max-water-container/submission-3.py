class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        l,r = 0, len(heights) - 1
        width = len(heights) - 1
        while l < r:
            volume = width * min(heights[l], heights[r])
            if volume > output:
                output = volume
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            width -= 1
        return output