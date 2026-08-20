class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int dist = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        unordered_set<int> seen;
        pq.push({0, 0});
        while (!pq.empty()) {
            pair<int, int> curr = pq.top();
            pq.pop();
            if (seen.count(curr.second)) {continue;}
            int u = curr.second;
            dist += curr.first;
            seen.insert(u);
            for (int i = 0; i < points.size(); i++) {
                if (seen.count(i)) {continue;}
                int d = abs(points[u][0] - points[i][0]) + abs(points[u][1] - points[i][1]);
                pq.push({d, i});
            }
        }
        return dist;
    }
};
