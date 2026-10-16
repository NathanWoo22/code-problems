class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums = sorted(nums)

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            curVal = nums[i]
            while i < len(nums) and nums[i] == curVal:
                i += 1
            dfs(i)
        
        dfs(0)
        return res
