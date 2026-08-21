class Solution {
public:
    unordered_map<char, unordered_set<char>> adj;
    unordered_map<char, bool> visited;
    string result;
    string foreignDictionary(vector<string>& words) {
        for (const string& w : words)
            for (char c : w)
                adj[c];
        for (int i = 0; i < (int)words.size() - 1; i++) {
            const string& w1 = words[i], & w2 = words[i + 1];
            int minLen = (int)min(w1.size(), w2.size());
            for (int j = 0; j < minLen; j++) {
                if (w1[j] != w2[j]) {
                    adj[w1[j]].insert(w2[j]);
                    break;
                }
                if (w1[j] == w2[j] and j == minLen - 1 and w1.size() > w2.size()) {
                    return "";
                }
            }
        }
        for (const auto& [key, values] : adj) {
            if (dfs(key)) {return "";}
        }
        reverse(result.begin(), result.end());
        return result;
    }
    bool dfs(char ch) {
        if (visited.count(ch)) {
            return visited[ch];
        }
        visited[ch]= true;
        for (const char next : adj[ch]) {
            if (dfs(next)) {return true;}
        }
        visited[ch] = false;
        result.push_back(ch);
        return false;
    }
};
