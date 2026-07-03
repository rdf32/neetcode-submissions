from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [[1, 0], [-1,0], [0,1], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        time = 0
        fresh = 0
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))

        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nrow, ncol = row + dr, col + dc

                    if nrow < 0 or nrow >= rows or ncol < 0 or ncol >= cols:
                        continue

                    if grid[nrow][ncol] == 1:
                        fresh -= 1
                        grid[nrow][ncol] = 2
                        queue.append((nrow, ncol))
            time += 1


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return time