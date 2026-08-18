class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int>& shortN = nums1.size() < nums2.size() ? nums1 : nums2;
        vector<int>& longN = nums1.size() < nums2.size() ? nums2 : nums1;
        int total = (int)(shortN.size() + longN.size());
        int half = (total + 1) / 2;
        int l = 0, r = (int)shortN.size();
        while (l <= r) {
            int i = l + (r - l) / 2;
            int j = half - i;
            int shortLeft = i > 0 ? shortN[i - 1] : INT_MIN;
            int shortRight = i < (int)shortN.size() ? shortN[i] : INT_MAX;
            int longLeft = j > 0 ? longN[j - 1] : INT_MIN;
            int longRight = j < (int)longN.size() ? longN[j] : INT_MAX;
            if (shortLeft <= longRight and longLeft <= shortRight) {
                if (total % 2) {
                    return (double)max(shortLeft, longLeft);
                } else {
                    return (max(shortLeft, longLeft) + min(shortRight, longRight)) / 2.0;
                }
            } else if (shortLeft > longRight) {
                r = i - 1;
            } else {
                l = i + 1;
            }
        }
        return 0;
    }
};
