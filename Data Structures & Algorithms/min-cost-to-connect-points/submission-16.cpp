class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        unordered_set<int> visited;
        int dist = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, 0});
        while (visited.size() < points.size()) {
            auto curr = pq.top();
            pq.pop();
            int u = curr.second;
            if (visited.count(u)) {continue;}
            dist += curr.first;
            visited.insert(u);
            if (visited.size() == points.size()) {break;}
            for (int i = 0; i < points.size(); i++) {
                if (visited.count(i)) {continue;}
                int d = abs(points[u][0] - points[i][0]) + abs(points[u][1] - points[i][1]);
                pq.push({d, i});
            }
        }
        return dist;
    }
};
