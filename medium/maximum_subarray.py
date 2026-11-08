class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxRunning = -float("infinity")
        longestFound = -float("infinity")
        for i in range(len(nums)):
            #At each point consider whether to keep current array or start new one, greedy almost.
            if nums[i] > maxRunning and maxRunning < 0:
                maxRunning = 0
            maxRunning += nums[i]
            longestFound = max(longestFound, maxRunning)
        return longestFound
