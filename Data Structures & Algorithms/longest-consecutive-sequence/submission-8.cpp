class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> items(nums.begin(), nums.end());
        int ans = 0;
        for (const int n : nums) {
            int target = n;
            if (items.find(target - 1) != items.end()) continue;
            size_t curr = 1;
            while (items.find(target + 1) != items.end()) {
                target++;
                curr++;
            }
            ans = std::max<int>(curr, ans);
        }
        return ans;
    }
};
