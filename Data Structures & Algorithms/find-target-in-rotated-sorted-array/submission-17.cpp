class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int l = nums[left], r = nums[right], m = nums[mid];
            if (m == target) {
                return mid;
            }
            // left-sorted
            if (m < r){ // right-sorted
                if (target > m and target <= r) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            } else {
                if (target >= l and target < m) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }
        return -1;
    }
};
