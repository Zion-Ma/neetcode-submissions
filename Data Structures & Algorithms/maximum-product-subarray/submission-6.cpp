class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max_prod = 1, min_prod = 1;
        int result = nums[0];
        for (int n : nums) {
            int temp_max = max_prod;
            max_prod = max({n, max_prod * n, min_prod * n});
            min_prod = min({n, temp_max * n, min_prod * n});
            result = max(result, max_prod);
        }
        return result;
    }
};
