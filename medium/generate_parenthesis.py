class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        subStr = ""
        def dfs(openCount, closeCount):
            nonlocal subStr
            if openCount == closeCount == n:
                res.append(subStr)
                return

            if closeCount < openCount: 
                subStr = subStr + ")"
                dfs(openCount, closeCount + 1)
                subStr = subStr[:-1]

            if openCount < n:
                subStr = subStr + "("
                dfs(openCount +1, closeCount)
                subStr = subStr[:-1]

        dfs(0, 0)

        return res
