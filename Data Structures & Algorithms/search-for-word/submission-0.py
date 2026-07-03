class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(row, col, index):
            if index == len(word):
                return True
            
            if (row < 0 or 
                row >= rows or 
                col < 0 or 
                col >= cols or
                board[row][col] != word[index] or
                (row, col) in visit):
                return False

            visit.add((row, col))
            res = (
                dfs(row + 1, col, index + 1) or
                dfs(row - 1, col, index + 1) or
                dfs(row, col - 1, index + 1) or
                dfs(row, col + 1, index + 1)
            )
            visit.remove((row, col))
            return res
        
        for r in range(rows): # start the search at each location
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
            
