class Solution {
public:
    int m;
    int n;
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        set<vector<int>> pac;
        set<vector<int>> atl;
        vector<vector<int>> result;
        m = (int)heights.size();
        n = (int)heights[0].size();
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
        set_intersection(
            pac.begin(), pac.end(),
            atl.begin(), atl.end(),
            back_inserter(result)
        );
        return result;
    }

    void search(int i, int j, int prev, set<vector<int>>& ocean, vector<vector<int>>& heights) {
        if (
            i >= m or i < 0 or\
            j >= n or j < 0 or\
            heights[i][j] < prev or\
            ocean.find({i, j}) != ocean.end()
        ) {return;}
        ocean.insert({i, j});
        vector<vector<int>> shift = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (const auto& d : shift) {
            search(i + d[0], j + d[1], heights[i][j], ocean, heights);
        }
    }
};
