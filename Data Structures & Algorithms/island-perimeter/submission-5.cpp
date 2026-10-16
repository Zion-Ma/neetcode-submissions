class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int perim = 0;
        for (int i = 0; i < m; i ++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {continue;}
                perim += 4;
                if (i > 0 and grid[i - 1][j] == 1) {perim -= 2;}
                if (j > 0 and grid[i][j - 1] == 1) {perim -= 2;}
            }
        }
        return perim;
    }
};