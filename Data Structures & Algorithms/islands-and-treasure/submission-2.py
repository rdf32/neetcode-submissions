class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        def dfs(row, col, count):

            if (row < 0 or row >= rows or
                col < 0 or col >= cols or
                grid[row][col] < count):
                return
            
            grid[row][col] = min(grid[row][col], count)
            dfs(row + 1, col, count + 1)
            dfs(row - 1, col, count + 1)
            dfs(row, col + 1, count + 1)
            dfs(row, col - 1, count + 1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    dfs(row, col, 0)
        
        


        