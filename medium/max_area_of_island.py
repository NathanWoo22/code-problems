class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        maxIslandSize = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j):
            nonlocal maxIslandSize
            stack = [[i, j]]
            islandSize = 0
            while stack: 
                node = stack.pop()
                islandSize += 1
                for d in dirs: 
                    m = [d[0] + node[0], d[1] + node[1]]
                    if (0 <= m[0] < ROWS and 0 <= m[1] < COLS and
                        grid[m[0]][m[1]] == 1):
                        grid[m[0]][m[1]] = 0
                        stack.append([m[0], m[1]])
            maxIslandSize = max(islandSize, maxIslandSize)


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    dfs(i, j)
        
        return maxIslandSize
                
