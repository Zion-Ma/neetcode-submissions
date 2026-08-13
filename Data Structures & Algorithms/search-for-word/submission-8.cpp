class Solution {
public:
    int target_length, m, n;
    bool exist(vector<vector<char>>& board, string word) {
        target_length = (int)word.size();
        m = (int)board.size();
        n = (int)board[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(i, j, 0, board, word)) {return true;}
            }
        }
        return false;
    }
    bool dfs(int i, int j, int k, vector<vector<char>>& board, string word) {
        if (k >= target_length) {return true;}
        if (
            i >= m or i < 0 or\
            j >= n or j < 0 or\
            board[i][j] != word[k]
        ) {return false;}
        char temp_char = board[i][j];
        board[i][j] = '.';
        if (
            dfs(i + 1, j, k + 1, board, word) or\
            dfs(i - 1, j, k + 1, board, word) or\
            dfs(i, j + 1, k + 1, board, word) or\
            dfs(i, j - 1, k + 1, board, word) 
        ) {return true;}
        board[i][j] = temp_char;
        return false;
    }
};
