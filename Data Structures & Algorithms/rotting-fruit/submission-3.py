class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1,0], [0,1], [0, -1]]

        num_fresh = 0
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    num_fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))

        total_time = 0
        while queue and num_fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nrow, ncol = row + dr, col + dc

                    if (nrow < 0 or nrow >= rows or ncol < 0 or ncol >= cols):
                        continue

                    if grid[nrow][ncol] == 1:
                        num_fresh -= 1
                        grid[nrow][ncol] = 2
                        queue.append((nrow, ncol)) ## find fresh make them rotten -- then process the rotten
                    
            total_time += 1

        return total_time if num_fresh <= 0 else -1


    