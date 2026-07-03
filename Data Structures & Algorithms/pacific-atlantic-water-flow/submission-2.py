class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(row, col, visit, prevHeight):

            if (
                (row, col) in visit or 
                row < 0 or 
                row >= rows or 
                col < 0 or 
                col >= cols or
                heights[row][col] < prevHeight
            ):
                return

            visit.add((row, col))
            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])


        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows - 1, col, atl, heights[rows-1][col])

        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols - 1, atl, heights[row][cols-1])
        
        res = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pac and (row, col) in atl:
                    res.append([row, col])
        
        return res




