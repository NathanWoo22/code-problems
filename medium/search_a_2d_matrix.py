
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        #find row
        upper = len(matrix) - 1
        lower = 0
        rowIdx = -1
        while lower <= upper:
            i = (lower + upper) // 2
            valLower = matrix[i][0]
            valHigher = matrix[i][-1]
            if target <= valHigher and target >= valLower:
                rowIdx = i
                break
            elif valLower < target:
                lower = i + 1
            elif valHigher > target: 
                upper = i - 1

        if rowIdx == -1:
            return False

        row = matrix[rowIdx]
        upper = len(row) - 1
        lower = 0
        while lower <= upper:
            i = (lower + upper) // 2
            val = row[i]
            if val < target:
                lower = i + 1
            elif val > target: 
                upper = i - 1
            else:
                return True
        
        return False
