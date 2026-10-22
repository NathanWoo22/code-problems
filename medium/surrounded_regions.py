class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        visited = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        saved = set() 
        stack = []
        for i in range(ROWS):
            if board[i][0] == "O":
                stack.append((i, 0))
            if board[i][COLS-1] == "O":
                stack.append((i, COLS - 1))
        
        for i in range(COLS):
            if board[0][i] == "O":
                stack.append((0, i))
            if board[ROWS - 1][i] == "O":
                stack.append((ROWS - 1, i))
            
        while stack: 
            nr, nc = stack.pop()
            visited[nr][nc] = 1
            saved.add((nr, nc))

            for dr, dc in dirs:
                mr, mc = dr + nr, dc + nc
                if (0 <= mr < ROWS and 0 <= mc < COLS
                    and visited[mr][mc] == 0 
                    and board[mr][mc] == "O"):
                    stack.append((mr, mc))

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i, j) not in saved:
                    board[i][j] = "X"
        

            
