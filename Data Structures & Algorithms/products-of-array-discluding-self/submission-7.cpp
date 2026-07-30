class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result = {1};
        for (int i = 1; i < nums.size(); i++) {
            int n = nums[i - 1];
            result.emplace_back(n * result[i - 1]);
        }
        int accumulate = 1;
        for (int i = nums.size() - 1; i > -1; i--) {
            result[i] = result[i] * accumulate;
            accumulate = accumulate * nums[i];
        }
        return result;
    }
};
