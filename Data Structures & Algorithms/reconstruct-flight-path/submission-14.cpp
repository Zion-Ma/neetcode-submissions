class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, vector<string>> adj;
        stack<string> stk;
        vector<string> result;
        sort(tickets.begin(), tickets.end());
        for (const auto& ticket : tickets) {
            adj[ticket[0]].push_back(ticket[1]);
        }
        for (auto& [src, dst] : adj) {
            sort(dst.rbegin(), dst.rend());
        }
        stk.push("JFK");
        while (!stk.empty()) {
            string curr = stk.top();
            if (adj[curr].empty()) {
                result.push_back(curr);
                stk.pop();
            } else {
                string next = adj[curr].back();
                adj[curr].pop_back();
                stk.push(next);
            }
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
