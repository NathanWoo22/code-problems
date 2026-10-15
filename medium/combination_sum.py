class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        combos = []
        subset = []
        def dfs(i, total):
            if  total == target:
                combos.append(subset.copy())
                return 
            elif total > target or i >= len(candidates):
                return 
            
            subset.append(candidates[i])
            total += candidates[i]
            dfs(i, total)

            subset.pop()
            total -= candidates[i]
            dfs(i + 1, total)
        
        dfs(0, 0)
        return combos
