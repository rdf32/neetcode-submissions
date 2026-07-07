class Solution {
    int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();

        int num_fresh = 0;
        std::queue<std::pair<int, int>> que;
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                int val = grid[row][col];
                if (val == 1) {
                    num_fresh++;
                } else if (val == 2) {
                    que.push({row, col});
                } else {continue;}
            }
        }

        int total = 0;
        while (!que.empty() && num_fresh > 0) {
            int n = que.size();
            for (int i = 0; i < n; i++){
                std::pair index = que.front();
                que.pop();
                for (const auto& dir: directions) {
                    int row = index.first + dir[0];
                    int col = index.second + dir[1];
                    if (row >= 0 && row < rows && 
                        col >= 0 && col < cols) {
                        int val = grid[row][col];
                        if (val == 1) {
                            num_fresh--;
                            grid[row][col] = 2;
                            que.push({row, col});
                        }
                    }
                }
            }
            total++;
        }
        return num_fresh == 0 ? total : -1;
    }
};
