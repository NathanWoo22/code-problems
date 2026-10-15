class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates = sorted(candidates)
        comboSet = []
        subset = []

        def dfs(i, total):
            if total == target:
                comboSet.append(subset.copy())
                return
            elif i >= len(candidates) or total + candidates[i] > target: 
                return
            
            
            subset.append(candidates[i])
            total += candidates[i]
            dfs(i + 1, total)

            subset.pop()
            total -= candidates[i]
            prev = candidates[i]
            i += 1
            while i < len(candidates) and prev == candidates[i]:
                i += 1
            
            dfs(i, total)

        dfs(0, 0)
        return comboSet
