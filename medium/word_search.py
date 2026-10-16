class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # find starts
        ROWS = len(board)
        COLS = len(board[0])

        starts = []
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    starts.append([i, j])
        
        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        good = False
        for start in starts: 
            visited = [[0 for x in range(COLS)] for x in range(ROWS)]
            def dfs(row, col, i):
                nonlocal good
                if i == len(word) - 1:
                    good = True
                    return True
                
                for d in dirs: 
                    m = [row + d[0], col + d[1]]
                    if (0 <= m[0] < ROWS and
                        0 <= m[1] < COLS and
                        visited[m[0]][m[1]] == 0 and
                        board[m[0]][m[1]] == word[i + 1]):
                            
                            visited[row][col] = 1
                            if dfs(m[0], m[1], i + 1):
                                return True
                            visited[row][col] = 0

            dfs(start[0], start[1], 0)


        return good
