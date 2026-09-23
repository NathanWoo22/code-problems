class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maxWater = (right - left) * min(height[left], height[right])
        while left != right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
            maxWater = max(maxWater, (right - left) * min(height[left], height[right]))

        return maxWater
            
