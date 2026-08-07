class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> adj(n + 1, vector<pair<int, int>>());
        vector<bool> visited(n + 1, false);
        vector<int> dist(n + 1, INT_MAX);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        int time = 0;
        dist[k] = 0;
        pq.push({0, k});
        for (const auto& t : times) {
            adj[t[0]].push_back({t[1], t[2]});
        }
        while (!pq.empty()) {
            auto curr = pq.top();
            pq.pop();
            int u = curr.second;
            if (visited[u]) {continue;}
            time = max(dist[u], time);
            for (const auto& nei : adj[u]) {
                int v = nei.first, w = nei.second;
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.push({dist[v], v});
                }
            }
        }
        for (int i = 1; i <= n; i++) {
            if (dist[i] == INT_MAX) {
                return -1;
            }
        }
        return time;
    }
};
