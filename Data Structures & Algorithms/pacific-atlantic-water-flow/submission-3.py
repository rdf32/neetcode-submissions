class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific_set = set()
        atlantic_set = set()

        rows, cols = len(heights), len(heights[0])
        def dfs(row, col, visit, prev_height):
            if ((row, col) in visit or
                row < 0 or row >= rows or
                col < 0 or col >= cols or 
                heights[row][col] < prev_height):
                return
            
            visit.add((row, col))
            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])

        for row in range(rows):
            dfs(row, 0, pacific_set, heights[row][0])
            dfs(row, cols - 1, atlantic_set, heights[row][cols - 1])
        
        for col in range(cols):
            dfs(0, col, pacific_set, heights[0][col])
            dfs(rows - 1, col, atlantic_set, heights[rows - 1][col])
        
        result  = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific_set and (row, col) in atlantic_set:
                    result.append([row, col])
        
        return result
