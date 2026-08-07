class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> indegree(numCourses, 0);
        vector<vector<int>> graph(numCourses, vector<int>());
        vector<int> result;
        for (const auto& p : prerequisites) {
            indegree[p[1]]++;
            graph[p[0]].push_back(p[1]);
        }
        queue<int> que;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                que.push(i);
            }
        }
        while (!que.empty()) {
            int curr = que.front();
            que.pop();
            result.push_back(curr);
            for (const int preq : graph[curr]) {
                indegree[preq]--;
                if (indegree[preq] == 0) {
                    que.push(preq);
                }
            }
        }
        if ((int)result.size() != numCourses) {
            return {};
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
