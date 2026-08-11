class Solution {
public:
    int m;
    int n;
    vector<vector<int>> shift;
    vector<vector<int>> result;
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        m = (int)heights.size();
        n = (int)heights[0].size();
        unordered_map<int, unordered_map<int, int>> pac;
        unordered_map<int, unordered_map<int, int>> atl;
        shift = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        // search row-wise
        for (int i = 0; i < m; i++) {
            // left-most column
            search(i, 0, -1, pac, heights);
            // right-most column
            search(i, n - 1, -1, atl, heights);
        }
        // search column-wise
        for (int j = 0; j < n; j++) {
            // top row
            search(0, j, -1, pac, heights);
            // bottom row
            search(m - 1, j, -1, atl, heights);
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pac[i][j] and atl[i][j]) {
                    result.push_back({i, j});
                }
            }
        }
        return result;
    }

    void search(int i, int j, int prev, unordered_map<int, unordered_map<int, int>>& ocean, vector<vector<int>>& heights) {
        if (
            i >= m or i < 0 or\
            j >= n or j < 0 or\
            heights[i][j] < prev or\
            (ocean.count(i) and ocean[i].count(j))
        ) {return;}
        ocean[i][j]++;
        for (const auto& d : shift) {
            search(i + d[0], j + d[1], heights[i][j], ocean, heights);
        }
    }
};
