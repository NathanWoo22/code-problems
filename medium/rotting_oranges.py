class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS = len(grid) 
        COLS = len(grid[0])

        rotten = []
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for i in range(ROWS):
            for j in range(COLS): 
                if grid[i][j] == 2:
                    rotten.append([i, j])

        # do bfs on all oranges and keep track of how much we go 
        time = 0 
        while rotten:
            curRotten = rotten 
            rotten = []

            for orange in curRotten: 
                for d in dirs:
                    m = [d[0] + orange[0], d[1] + orange[1]]
                    if (0 <= m[0] < ROWS and 0 <= m[1] < COLS
                        and grid[m[0]][m[1]] == 1):
                        rotten.append(m)
                        grid[m[0]][m[1]] = 2
            if rotten:
                time += 1

            
        for i in range(ROWS):
            for j in range(COLS): 
                if grid[i][j] == 1:
                    return -1
        
        return time
