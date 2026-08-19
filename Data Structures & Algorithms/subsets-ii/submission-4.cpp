class Solution {
public:
    vector<vector<int>> result;
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> curr;
        dfs(0, curr, nums);
        return result;
    }
    void dfs(int i, vector<int> curr, vector<int>& nums) {
        if (i == nums.size()) {
            result.push_back(curr);
            return;
        }
        curr.push_back(nums[i]);
        dfs(i + 1, curr, nums);
        curr.pop_back();
        while (i + 1 < nums.size() and nums[i] == nums[i + 1]) {
            i++;
        }
        dfs(i + 1, curr, nums);
    }
};
