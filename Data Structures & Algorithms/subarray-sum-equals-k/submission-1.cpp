class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int total = 0;
        int currSum = 0;
        unordered_map<int, int> prefixSum = {{0, 1}};
        for (int n : nums) {
            currSum += n;
            int diff = currSum - k;
            total += prefixSum[diff];
            prefixSum[currSum]++;
        }
        return total;
    }
};