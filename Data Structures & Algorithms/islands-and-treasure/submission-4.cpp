class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        queue<vector<int>> source;
        std::set<vector<int>> seen;
        vector<vector<int>> shift = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int dist = 1;
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    source.push({i, j});
                    seen.insert({i, j});
                }
            }
        }
        while (!source.empty()) {
            int len = (int)source.size();
            for (int i = 0; i < len; i++) {
                vector<int> curr = source.front();
                source.pop();
                for (auto& d : shift) {
                    int r = curr[0] + d[0];
                    int c = curr[1] + d[1];
                    if (
                        (r >= m or r < 0) or\
                        (c >= n or c < 0) or\
                        grid[r][c] != INT_MAX or\
                        seen.find({r, c}) != seen.end()
                    ) {continue;}
                    grid[r][c] = dist;
                    source.push({r, c});
                    seen.insert({r, c});
                }
            }
            dist++;
        }
    }
};
