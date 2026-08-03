class Solution {
public:
    vector<int> status;
    unordered_map<int, vector<int>> record;
    vector<int> result;
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        status.assign(numCourses, 0);
        for (const auto& p : prerequisites) {
            record[p[0]].push_back(p[1]);
        }
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i)) {return {};}
        }
        return result;
    }
    bool dfs(int i) {
        if (status[i] == 2) {
            return true;
        }
        if (status[i] == 1) {
            return false;
        }
        status[i] = 1;
        for (const int nei : record[i]) {
            if (!dfs(nei)) {return false;}
        }
        status[i] = 2;
        result.push_back(i);
        return true;
    }
};
