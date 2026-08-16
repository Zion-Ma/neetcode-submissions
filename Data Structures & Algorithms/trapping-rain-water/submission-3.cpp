class Solution {
public:
    int trap(vector<int>& height) {
        vector<int> prefix((int)height.size(), 0);
        vector<int> suffix((int)height.size(), 0);
        int result = 0;
        prefix[0] = max(height[0], prefix[0]);
        for (int i = 1; i < height.size(); i++) {
            prefix[i] = max(prefix[i - 1], height[i]);
        }
        suffix.back() = max(suffix.back(), height.back());
        for (int i = (int)height.size() - 2; i > -1; i--) {
            suffix[i] = max(suffix[i + 1], height[i]);
        }
        for (int i = 1; i < height.size() - 1; i++) {
            int volume = min(prefix[i], suffix[i]);
            result += max(volume - height[i], 0);
        }
        return result;
    }
};
