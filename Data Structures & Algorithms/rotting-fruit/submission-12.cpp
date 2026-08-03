class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int fresh = 0, minute = 0;
        int m = (int)grid.size(), n = (int)grid[0].size();
        queue<vector<int>> source;
        vector<vector<int>> shift = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    fresh++;
                } else if (grid[i][j] == 2) {
                    source.push({i, j});
                }
            }
        }
        while (fresh > 0 and !source.empty()) {
            int len = (int)source.size();
            for (int i = 0; i < len; i++) {
                vector<int> curr = source.front();
                source.pop();
                for (auto& p : shift) {
                    int r = curr[0] + p[0];
                    int c = curr[1] + p[1];
                    if (
                        (r >= m or r < 0) or\
                        (c >= n or c < 0) or\
                        grid[r][c] != 1
                    ) {continue;}
                    grid[r][c] = 2;
                    fresh--;
                    source.push({r, c});
                }
            }
            minute++;
        }
        return (fresh == 0 ? minute: -1);
    }
};
