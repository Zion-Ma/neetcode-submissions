class Solution {
public:
    vector<vector<int>> result;
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> curr = {};
        dfs(0, target, curr, nums);
        return result;
    }
    void dfs(int i, int target, vector<int>& curr, vector<int>& nums) {
        if (target == 0) {
            result.push_back(curr);
            return;
        }
        if (i >= nums.size() or target < 0) {
            return;
        }
        curr.push_back(nums[i]);
        dfs(i, target - nums[i], curr, nums);
        curr.pop_back();
        dfs(i + 1, target, curr, nums);
    }
};
