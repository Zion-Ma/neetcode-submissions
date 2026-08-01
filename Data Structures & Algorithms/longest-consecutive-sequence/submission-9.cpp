class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> record(nums.begin(), nums.end());
        int ans = 0;
        for (const int num : record) {
            int n = num;
            if (record.find(n - 1) != record.end()) {continue;}
            int count = 1;
            while (record.find(n + 1) != record.end()) {
                count++;
                n++;
            }
            ans = std::max(ans, count);
        }
        return ans;
    }
};
