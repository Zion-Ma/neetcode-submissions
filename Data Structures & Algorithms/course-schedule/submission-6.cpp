#include <iostream>
#include <vector>
#include <numeric> // Required for std::accumulate

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> indegree(numCourses, 0);
        vector<vector<int>> graph(numCourses, vector<int>());
        vector<int> result;
        for (auto& p : prerequisites) {
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
            for (const int nei : graph[curr]) {
                indegree[nei]--;
                if (indegree[nei] == 0) {
                    que.push(nei);
                }
            }
        }

        return accumulate(indegree.begin(), indegree.end(), 0) == 0;
    }
};
