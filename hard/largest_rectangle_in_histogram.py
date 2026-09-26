class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        leftBoundary = [0] * len(heights)
        rightBoundary = [0] * len(heights)

        def findBoundary(heights):
            stack = []
            boundary = [0] * len(heights)
            for i, h in enumerate(heights):
                if len(stack) == 0:
                    stack.append([h, i])
                else:
                    while len(stack) > 0 and h < stack[-1][0]:
                        val = stack.pop()
                        boundary[val[1]] = i 

                    stack.append([h, i])
                
            for i, s in enumerate(stack):
                boundary[s[1]] = len(heights) 

            return boundary

        rightBoundary = findBoundary(heights)
        leftBoundary = [len(heights) - x for x in findBoundary(heights[::-1])][::-1]
        maxHist = 0
        for i, h in enumerate(heights):
            area = h * (rightBoundary[i] - leftBoundary[i]) 
            maxHist = max(maxHist, area)

        return maxHist

