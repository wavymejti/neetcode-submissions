class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        minimalHeight = [0] * len(height)
        maxHeight = 0
        output = 0
        volume = 0
        l, r = 0, len(height) - 1
        for i in range(len(height)):
            maxLeft[i] = maxHeight
            maxHeight = max(height[i], maxHeight)
        maxHeight = 0
        for i in range(len(height) -1,-1,-1):
            maxRight[i] = maxHeight
            maxHeight = max(height[i], maxHeight)
        for i in range(len(height)):
            minimalHeight[i] = min(maxLeft[i], maxRight[i])
        for i in range(len(height)):
            volume = minimalHeight[i] - height[i]
            if volume > 0:
                output += volume

        return output