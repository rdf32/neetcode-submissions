class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_sets = {i: set() for i in range(9)}
        col_sets = {i: set() for i in range(9)}
        squ_sets = {i: set() for i in range(9)}

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                value = board[row][col]
                if (value in row_sets[row] or 
                    value in col_sets[col] or 
                    value in squ_sets[(row // 3) * 3 + (col // 3)]):
                    return False

                row_sets[row].add(value)
                col_sets[col].add(value)
                squ_sets[(row // 3) * 3 + (col // 3)].add(value)

        return True

