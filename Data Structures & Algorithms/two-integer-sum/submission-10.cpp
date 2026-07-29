class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> records;
        for (int i = 0; i < nums.size(); i++){
            int diff = target - nums[i];
            if (records.find(diff) != records.end()) {
                return {records[diff], i};
            }
            records.insert({nums[i], i});
        }
        return {};
    }
};
