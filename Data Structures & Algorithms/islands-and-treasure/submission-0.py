class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, d):

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            if grid[r][c] < d:
                return
                
            grid[r][c] = d

            for dr, dc in directions:
                dfs(r + dr, c + dc, d + 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    dfs(row, col, 0)

        return