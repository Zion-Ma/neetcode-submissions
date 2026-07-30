class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for (int curr = 0; curr < nums.size(); curr++) {
            if (nums[curr] > 0) break;
            int n = nums[curr];
            if (curr > 0 and n == nums[curr - 1]) continue;
            int left = curr + 1;
            int right = nums.size() - 1;
            while (left < right) {
                int sum = n + nums[left] + nums[right];
                if (sum > 0) right--;
                else if (sum < 0) left++;
                else {
                    result.push_back({n, nums[left], nums[right]});
                    while (left < right and nums[left] == nums[left + 1]) left++;
                    left++;
                    right--;
                }
            }
        }
        return result;
    }
};
