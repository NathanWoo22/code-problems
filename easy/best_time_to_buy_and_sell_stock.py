class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0 
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] - prices[l] > profit:
                profit = prices[r] - prices[l]
            elif prices[r] < prices[l]:
                l = r
            else: 
                r = r + 1
        return profit
