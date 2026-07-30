class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for (int curr = 0; curr < nums.size(); curr++) {
            if (nums[curr] > 0) break;
            if (curr > 0 and nums[curr] == nums[curr - 1]) continue;
            int target = 0 - nums[curr];
            int left = curr + 1;
            int right = nums.size() - 1;
            while (left < right) {
                int sum = nums[left] + nums[right];
                if (sum > target) {
                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    result.push_back({nums[curr], nums[left], nums[right]});
                    
                    while (left < right and nums[left] == nums[left + 1]) {
                        left++;
                    }
                    left++;
                    right--;
                }
            }
        }
        return result;
    }
};
