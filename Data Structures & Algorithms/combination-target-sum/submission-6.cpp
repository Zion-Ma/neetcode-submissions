class Solution {
public:
    vector<vector<int>> result;
    int max_len;
    int t;
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        max_len = (int)nums.size();
        t = target;
        vector<int> curr = {};
        dfs(0, 0, curr, nums);
        return result;
    }
    void dfs(int i, int curr_sum, vector<int>& curr, vector<int>& nums) {
        if (curr_sum == t) {
            result.push_back(curr);
            return;
        }
        if (i >= max_len or curr_sum > t) {
            return;
        }
        curr.push_back(nums[i]);
        dfs(i, curr_sum + nums[i], curr, nums);
        curr.pop_back();
        dfs(i + 1, curr_sum, curr, nums);
    }
};
