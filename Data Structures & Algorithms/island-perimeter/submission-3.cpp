class Solution {
public:
    unordered_map<int, unordered_set<int>> visited;
    int m, n;
    int islandPerimeter(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    return dfs(i, j, grid);
                }
            }
        }
        return 0;
    }
    int dfs(int i, int j, vector<vector<int>>& grid) {
        if (i >= m or i < 0 or j >= n or j < 0 or grid[i][j] == 0) {
            return 1;
        }
        if (visited.contains(i) and visited.at(i).contains(j)) {
            return 0;
        }
        visited[i].insert(j);
        return dfs(i + 1, j, grid) + dfs(i - 1, j, grid) + dfs(i, j + 1, grid) + dfs(i, j - 1, grid);
    }
};