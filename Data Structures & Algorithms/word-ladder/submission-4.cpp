class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if (beginWord == endWord) {return 1;}
        if (find(wordList.begin(), wordList.end(), endWord) == wordList.end()) {return 0;}
        unordered_map<string, vector<string>> graph;
        queue<string> que;
        unordered_set<string> seen;
        int count = 1;
        for (const string s : wordList) {
            for (int i = 0; i < s.size(); i++) {
                const string key = s.substr(0, i) + '*' + s.substr(i + 1);
                graph[key].push_back(s);
            }
        }
        que.push(beginWord);
        seen.insert(beginWord);
        while (!que.empty()) {
            int sz = (int)que.size();
            for (int i = 0; i < sz; i++) {
                string curr = que.front();
                que.pop();
                if (curr == endWord) {return count;}
                for (int j = 0; j < curr.size(); j++) {
                    const string key = curr.substr(0, j) + '*' + curr.substr(j + 1);
                    if (!graph.count(key)) {continue;}
                    for (const string nei : graph.at(key)) {
                        if (seen.count(nei)) {continue;}
                        que.push(nei);
                        seen.insert(nei);
                    }
                    graph.erase(key);
                }
            }
            count++;
        }
        return 0;
    }
};
