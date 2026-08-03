class Solution {
public:
    vector<vector<int>> result;
    int len;
    vector<vector<int>> subsets(vector<int>& nums) {
        len = (int)nums.size();
        vector<int> curr; 
        dfs(0, curr, nums);
        return result;
    }
    void dfs(int idx, vector<int>& curr, vector<int>& nums) {
        if (idx == len) {
            result.emplace_back(curr);
            return;
        }
        curr.push_back(nums[idx]);
        dfs(idx + 1, curr, nums);
        curr.pop_back();
        dfs(idx + 1, curr, nums);
    }
};
