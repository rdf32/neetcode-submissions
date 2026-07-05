class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();

        int max_area = 0;
        for (int row = 0; row < rows; row++){
            for (int col = 0; col < cols; col++){
                if (grid[row][col] == 1){
                    int area = dfs(grid, row, col);
                    max_area = std::max(max_area, area);
                }
            }
        }

        return max_area;
    }

    int dfs(vector<vector<int>>& grid, int row, int col) {
        int rows = grid.size();
        int cols = grid[0].size();

        if (row < 0 || row >= rows ||
            col < 0 || col >= cols ||
            grid[row][col] == 0) {return 0;}

        grid[row][col] = 0;
        int area = 1;
        area += dfs(grid, row + 1, col);
        area += dfs(grid, row - 1, col);
        area += dfs(grid, row, col + 1);
        area += dfs(grid, row, col - 1);
        return area;
    }
};
