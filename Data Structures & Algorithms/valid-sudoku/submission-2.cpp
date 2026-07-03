class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        
        std::unordered_map<int, std::set<char>> rows;
        std::unordered_map<int, std::set<char>> cols;
        std::unordered_map<int, std::set<char>> sqrs;

        for (int row = 0; row < 9; row++){
            for (int col = 0; col < 9; col++){
                char c = board[row][col];
                if (c == '.') continue;

                if (
                    rows[row].count(c) || 
                    cols[col].count(c) || 
                    sqrs[(row / 3) * 3 + (col / 3)].count(c)
                    ) return false;
                
                rows[row].insert(c);
                cols[col].insert(c);
                sqrs[(row / 3) * 3 + (col / 3)].insert(c);

            }

        }
        return true;

    }
};
