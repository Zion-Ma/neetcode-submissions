class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) {break;}
            if (i > 0 and nums[i] == nums[i - 1]) {continue;}
            int curr = nums[i];
            int left = i + 1, right = (int)nums.size() - 1;
            while (left < right) {
                int sum = curr + nums[left] + nums[right];
                if (sum > 0) {
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    result.push_back({curr, nums[left], nums[right]});
                    // do skip first. otherwise, it will kill possible ans with repeated values
                    while (left < right and nums[left] == nums[left + 1]) {left++;}
                    left++;
                    right--;
                }
            }
        }
        return result;
    }
};
