class Solution {
public:
    bool canJump(vector<int>& nums) {
        int max_reach = 0;
        int i = 0;
        while (i < (int)nums.size() and max_reach < (int)nums.size() - 1) {
            if (max_reach < i) {
                return false;
            } else {
                max_reach = max(max_reach, nums[i] + i);
                i++;
            }
        }
        return i < (int)nums.size();
    }
};
