// #include <numeric> 

class Solution {
public:
    int len;
    int t;
    vector<vector<int>> result;
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        len = (int)candidates.size();
        t = target;
        vector<int> curr;
        sort(candidates.begin(), candidates.end());
        dfs(0, curr, candidates);
        return result;
    }
    void dfs(int idx, vector<int>& curr, vector<int>& candidates) {
        if (std::accumulate(curr.begin(), curr.end(), 0) == t) {
            result.emplace_back(curr);
            return;
        }
        if (idx >= len or std::accumulate(curr.begin(), curr.end(), 0) > t) {
            return;
        }
        curr.push_back(candidates[idx]);
        dfs(idx + 1, curr, candidates);
        curr.pop_back();
        while (idx + 1 < len and candidates[idx] == candidates[idx + 1]) {
            idx++;
        }
        dfs(idx + 1, curr, candidates);
    }
};
