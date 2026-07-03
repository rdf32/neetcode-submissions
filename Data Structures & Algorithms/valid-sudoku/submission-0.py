class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows, cols = len(board), len(board[0])

        rowsets = {i: set() for i in range(rows)}
        colsets = {i: set() for i in range(cols)}
        squaresets = {}
        for row in range(rows // 3):
            for col in range(cols // 3):
                squaresets[(row, col)] = set()

        for row in range(rows):
            for col in range(cols):
                value = board[row][col]
                if value == '.':
                    continue
                if value in rowsets[row] or value in colsets[col] or value in squaresets[(row // 3, col // 3)]:
                    return False

                rowsets[row].add(value)
                colsets[col].add(value)
                squaresets[(row // 3, col // 3)].add(value)
        return True
