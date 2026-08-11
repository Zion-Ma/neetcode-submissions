class CountSquares {
public:
    unordered_map<int, unordered_map<int, int>> records;
    CountSquares() {}
    
    void add(vector<int> point) {
        records[point[0]][point[1]]++;
    }
    
    int count(vector<int> point) {
        int ans = 0;
        int ox = point[0], oy = point[1];
        for (const auto& [diagx, y_cand] : records) {
            for (const auto& [diagy, freq] : y_cand) {
                if (diagx == ox or diagy == oy or abs(ox - diagx) != abs(oy - diagy)) {
                    continue;
                }
                if (records[diagx].count(oy) and records[ox].count(diagy)) {
                    ans += (freq * records[diagx][oy] * records[ox][diagy]);
                }
            }
        }
        return ans;
    }
};
