class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<int> dist(n + 1, INT_MAX);
        unordered_set<int> seen;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        unordered_map<int, vector<pair<int, int>>> graph;
        int time = -1;
        for (const auto& item : times) {
            int u = item[0], v = item[1], t = item[2];
            graph[u].push_back({t, v});
        }
        pq.push({0, k});
        dist[k] = 0;
        while (!pq.empty()) {
            pair<int, int> curr = pq.top();
            pq.pop();
            int u = curr.second;
            if (seen.count(u)) {continue;}
            // no need to pre-insert k; remember to insert u after check
            seen.insert(u);
            time = curr.first;
            for (const auto& [w, v] : graph[u]) {
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.push({dist[v], v});
                }
            }
        }
        // remember 0 is dummy
        for (int i = 1; i < dist.size(); i++) {
            if (dist[i] == INT_MAX) {return -1;}
        }
        return time;
    }
};
