class Solution {
public:
    int m;
    int n;
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;
        m = (int)grid.size();
        n = (int)grid[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    maxArea = max(maxArea, area(i, j, grid));
                }
            }
        }
        return maxArea;
    }
    int area(int i, int j, vector<vector<int>>& grid) {
        if (
            i >= m or i < 0 or\
            j >= n or j < 0 or\
            grid[i][j] != 1
        ) {return 0;}
        grid[i][j] = 0;
        return 1 + area(i + 1, j, grid) + area(i - 1, j, grid) + area(i, j + 1, grid) + area(i, j - 1, grid);
    }
};
