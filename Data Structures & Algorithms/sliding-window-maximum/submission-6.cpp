class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        priority_queue<pair<int, int>> max_heap;
        vector<int> result;
        for (int i = 0; i < k; i++) {
            max_heap.push({nums[i], i});
        }
        result.push_back(max_heap.top().first);
        for (int i = k; i < nums.size(); i++) {
            while (!max_heap.empty() and max_heap.top().second < i - k + 1) {
                max_heap.pop();
            }
            max_heap.push({nums[i], i});
            result.push_back(max_heap.top().first);
        }
        return result;
    }
};
