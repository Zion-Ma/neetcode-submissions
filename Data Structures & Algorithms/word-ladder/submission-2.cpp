class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if (beginWord == endWord or find(wordList.begin(), wordList.end(), endWord) == wordList.end()){
            return 0;
        }
        unordered_map<string, vector<string>> adj;
        unordered_set<string> seen;
        queue<string> que;
        int hop = 1;
        for (const string& s : wordList) {
            for (int i = 0; i < s.size(); i ++) {
                string key = s.substr(0, i) + '*' + s.substr(i + 1);
                adj[key].push_back(s);
            }
        }
        seen.insert(beginWord);
        que.push(beginWord);
        while (!que.empty()) {
            int sz = que.size();
            for (int i = 0; i < sz; i++) {
                string curr = que.front();
                que.pop();
                for (int j = 0; j < curr.size(); j++) {
                    string key = curr.substr(0, j) + '*' + curr.substr(j + 1);
                    if (!adj.count(key)) {continue;}
                    for (const string& s : adj[key]) {
                        if (s == endWord) {return hop + 1;}
                        if (seen.count(s)) {continue;}
                        que.push(s);
                        seen.insert(s);
                    }
                    adj.erase(key);
                }
            }
            hop++;
        }
        return 0;
    }
};
