class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        lowerMin = cost[0]
        upperMin = cost[1]

        for i in range(2, len(cost)):
            temp = cost[i] + min(lowerMin, upperMin)
            lowerMin = upperMin
            upperMin = temp
        
        return min(lowerMin, upperMin)
