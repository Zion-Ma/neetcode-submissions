class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<char>> row;
        unordered_map<int, unordered_set<char>> col;
        unordered_map<int, unordered_set<char>> box;

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') continue;
                if (row[i].find(board[i][j]) != row[i].end()) return false;
                if (col[j].find(board[i][j]) != col[j].end()) return false;
                if (box[(i / 3) * 3 + j / 3].find(board[i][j]) != box[i / 3 + j / 3].end()) return false;
                row[i].insert(board[i][j]);
                col[j].insert(board[i][j]);
                box[(i / 3) * 3 + j / 3].insert(board[i][j]);
            }
        } 
        return true;
    }
};
