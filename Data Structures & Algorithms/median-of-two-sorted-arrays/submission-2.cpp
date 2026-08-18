class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int>& shortN = nums1.size() < nums2.size() ? nums1 : nums2;
        vector<int>& longN = nums1.size() < nums2.size() ? nums2 : nums1;
        int total = shortN.size() + longN.size();
        int half = (total + 1) / 2;
        int l = 0, r = shortN.size();
        while (l <= r) {
            // target number of elements in shortN
            int target_short = l + (r - l) / 2;
            // target number of elements in longN
            int target_long = half - target_short;
            int shortLeft = target_short > 0 ? shortN[target_short - 1] : INT_MIN;
            int shortRight = target_short < shortN.size() ? shortN[target_short] : INT_MAX;
            int longLeft = target_long > 0 ? longN[target_long - 1] : INT_MIN;
            int longRight = target_long < longN.size() ? longN[target_long] : INT_MAX;
            if (shortLeft <= longRight and longLeft <= shortRight) {
                if (total % 2) {
                    return (double)max(shortLeft, longLeft);
                } else {
                    return (max(shortLeft, longLeft) + min(longRight, shortRight)) / 2.0;
                }
            } else if (shortLeft > longRight) {
                r = target_short - 1;
            } else {
                l = target_short + 1;
            }
        }
        return 0;
    }
};
