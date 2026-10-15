class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def perms(subset):
            if len(subset) == 0:
                return [[]]
            
            curPerms = perms(subset[1:])
            res = []
            for perm in curPerms:
                for i in range(len(perm) + 1):
                    permCopy = perm.copy()
                    permCopy.insert(i, subset[0])
                    res.append(permCopy)

            return res
            
        return perms(nums)
        
            

            
