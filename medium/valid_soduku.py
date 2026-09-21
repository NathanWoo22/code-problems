class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(lambda: defaultdict(set))
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in rows[i]:
                    return False
                
                if board[i][j] in cols[j]:
                    return False
                
                if board[i][j] in boxes[i//3][j//3]:
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[i//3][j//3].add(board[i][j])  
        return True
