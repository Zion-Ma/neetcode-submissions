class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        vector<bool> visited((int)points.size(), false);
        int dist = 0;
        int count = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, 0});
        while (count < (int)points.size()) {
            auto curr = pq.top();
            pq.pop();
            int u = curr.second;
            if (visited[u]) {continue;}
            visited[u] = true;
            count++;
            dist += curr.first;
            if (count == (int)points.size()) {break;}
            for (int i = 0; i < points.size(); i++) {
                if (visited[i]) {continue;}
                int d = abs(points[u][0] - points[i][0]) + abs(points[u][1] - points[i][1]);
                pq.push({d, i});
            }
        }
        return dist;
    }
};
