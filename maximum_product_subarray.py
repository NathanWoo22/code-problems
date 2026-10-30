class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxCache = [0] * len(nums)
        maxVal = nums[0]
        
        def dfs(i):
            nonlocal maxVal

            if i == len(nums) -1:
                maxVal = max(maxVal, nums[-1])
                return (nums[-1], nums[-1])
            
            if maxCache[i] != 0:
                return maxCache[i]

            minRes, maxRes = dfs(i + 1)    
            minProduct = min(nums[i], nums[i] * maxRes, nums[i] * minRes)
            maxProduct = max(nums[i], nums[i] * maxRes, nums[i] * minRes)
            maxVal = max(maxVal, maxProduct)

            maxCache[i] = (minProduct, maxProduct)
            return (minProduct, maxProduct)
        
        dfs(0)
        return maxVal
