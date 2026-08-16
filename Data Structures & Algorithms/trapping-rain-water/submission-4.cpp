class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0, r = (int)height.size() - 1;
        int leftMax = height[0], rightMax = height.back();
        int result = 0;
        while (l < r) {
            if (leftMax < rightMax) {
                l++;
                leftMax = max(leftMax, height[l]);
                result += leftMax - height[l];
            } else {
                r--;
                rightMax = max(rightMax, height[r]);
                result += rightMax - height[r];
            }
        }
        return result;
    }
};
