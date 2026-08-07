class Solution {
public:
    void solve(vector<vector<char>>& board) {
        queue<vector<int>> circles;
        int m = (int)board.size(), n = (int)board[0].size();
        vector<vector<int>> shift = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        // mask out the outer unsurrounded
        for (int i = 0; i < m; i++) {
            for (int j : {0, n - 1}) {
                if (board[i][j] == 'O') {
                    circles.push({i, j});
                    board[i][j] = '.';
                }
            }
        }
        for (int j = 0; j < n; j++) {
            for (int i : {0, m - 1}) {
                if (board[i][j] == 'O') {
                    circles.push({i, j});
                    board[i][j] = '.';
                }
            }
        }
        // mask out O that can be reached from outer unsurrounded
        while (!circles.empty()) {
            int curr_size = (int)circles.size();
            for (int i = 0; i < curr_size; i++) {
                vector<int> curr = circles.front();
                circles.pop();
                for (const auto& p : shift) {
                    int r = curr[0] + p[0];
                    int c = curr[1] + p[1];
                    if (
                        r >= m or r < 0 or\
                        c >= n or c < 0 or\
                        board[r][c] != 'O'
                    ) {continue;}
                    board[r][c] = '.';
                    circles.push({r, c});
                }
            }
        }
        // mark surrounded with X and recover unsurrounded
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                } else if (board[i][j] == '.') {
                    board[i][j] = 'O';
                }
            }
        }
    }
};
