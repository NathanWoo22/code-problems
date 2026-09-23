class Solution:
    def trap(self, height: list[int]) -> int:
        maxLeft = [height[0]]
        maxRight = [height[-1]]
        for i in range(1, len(height), 1):
            maxLeft.append(max(maxLeft[i-1], height[i]))
        for i in range(len(height)-2, -1, -1):
            maxRight.insert(0, max(maxRight[0], height[i]))
            
        total = 0 
        for i, h in enumerate(height):
            lowh = min(maxLeft[i], maxRight[i])
            if lowh > h:
                total += lowh-h

        return total
