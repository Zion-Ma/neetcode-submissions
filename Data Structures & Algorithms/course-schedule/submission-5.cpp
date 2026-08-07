class Solution {
public:
    vector<int> status;
    vector<vector<int>> graph;
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        status.assign(numCourses, 0);
        graph.assign(numCourses, vector<int>());
        for (const auto& p : prerequisites) {
            graph[p[0]].push_back(p[1]);
        }
        // dfs
        for (int course = 0; course < numCourses; course++) {
            if (!dfs(course)) {
                return false;
            }
        }
        return true;
    }
    bool dfs(int course) {
        // 2: visted; it's good
        if (status[course] == 2) {
            return true;
        }
        // 1: being visited; circle found
        if (status[course] == 1) {
            return false;
        }
        status[course] = 1;
        for (const int nei : graph[course]) {
            if (!dfs(nei)) {
                return false;
            }
        }
        status[course] = 2;
        return true;
    }
};
