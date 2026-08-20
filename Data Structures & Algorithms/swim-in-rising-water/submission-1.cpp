class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
        unordered_map<int, unordered_set<int>> seen;
        vector<pair<int, int>> shift = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        pq.push({grid[0][0], {0, 0}});
        int m = (int)grid.size(), n = (int)grid[0].size();
        while (!pq.empty()) {
            pair<int, pair<int, int>> curr = pq.top();
            pq.pop();
            int t = curr.first;
            int r = curr.second.first, c = curr.second.second;
            if (seen.count(r) and seen.at(r).count(c)) {continue;}
            seen[r].insert(c);
            if (r == m - 1 and c == n - 1) {
                return max(t, grid[r][c]);
            }
            for (const auto& s : shift) {
                int x = r + s.first, y = c + s.second;
                if (x >= m or x < 0 or y >= n or y < 0) {continue;}
                pq.push({max(t, grid[x][y]), {x, y}});
            }
        }
        return 0;

    }
};
