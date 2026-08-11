class CountSquares {
public:
    unordered_map<int, unordered_map<int, int>> records;
    CountSquares() {}
    
    void add(vector<int> point) {
        records[point[0]][point[1]]++;
    }
    
    int count(vector<int> point) {
        int ans = 0;
        int px = point[0], py = point[1];
        for (const auto& [diagx, y_cand] : records) {
            for (const auto& [diagy, freq] : y_cand) {
                if (px == diagx or py == diagy or abs(px - diagx) != abs(py - diagy)) {
                    continue;
                }
                if (records[px].count(diagy) and records[diagx].count(py)) {
                    ans += (freq * records[px][diagy] * records[diagx][py]);
                }
            }
        }
        return ans;
    }
};
