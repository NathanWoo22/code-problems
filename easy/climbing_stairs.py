class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        resList = [0] * (n + 1) 
        resList[n] = 0
        resList[n-1] = 1
        resList[n-2] = 2
        i = n-3
        while i >= 0:
            resList[i] = resList[i + 1] + resList[i + 2]
            i -= 1
        return resList[0]
