class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or
                grid[row][col] == "0"):
                return False

            grid[row][col] = "0"
            for rd, cd in directions:
                dfs(row + rd, col + cd)

            return True
        
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col):
                    islands += 1
        
        return islands