class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for i in range(ROWS):
            for j in range(COLS):
                # Find island and go from there
                if grid[i][j] == "1" and visited[i][j] == 0:
                    # run bfs 
                    islands += 1
                    stack = [[i, j]]
                    while stack:
                        val = stack.pop()
                        for d in dirs: 

                            m = [d[0] + val[0], d[1] + val[1]]
                            if (0 <= m[0] < ROWS and 0 <= m[1] < COLS
                                and visited[m[0]][m[1]] == 0
                                and grid[m[0]][m[1]] == "1"):
                                visited[m[0]][m[1]] = 1
                                stack.append(m)

        return islands
