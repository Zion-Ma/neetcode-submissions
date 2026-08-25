class Solution {
public:
    unordered_map<char, bool> being_visited;
    unordered_map<char, unordered_set<char>> adj;
    string result;
    string foreignDictionary(vector<string>& words) {
        for (const string& w : words){
            for (char c : w) adj[c];
        }
        for (int i = 1; i < words.size(); i++) {
            string w1 = words[i - 1], w2 = words[i];
            int minLen = min((int)w1.size(), (int)w2.size());
            for (int j = 0; j < minLen; j++) {
                if (w1[j] != w2[j]) {
                    adj[w1[j]].insert(w2[j]);
                    break;
                }
                if (j == minLen - 1 and w1[j] == w2[j] and w1.size() > w2.size()) {
                    return "";
                }
            }
        }
        for (const auto& [key, values] : adj) {
            if (dfs(key)) {
                return "";
            }
        }
        reverse(result.begin(), result.end());
        return result;
    }
    bool dfs(char c) {
        if (being_visited.count(c)) {
            return being_visited[c];
        }
        being_visited[c] = true;
        for (const char nei : adj[c]) {
            if (dfs(nei)) {
                return true;
            }
        }
        being_visited[c] = false;
        result.push_back(c);
        return false;
    }
};
