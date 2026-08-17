class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        priority_queue<pair<int, int>> max_heap;
        vector<int> answer;
        for (int i = 0; i < nums.size(); i++) {
            max_heap.push({nums[i], i});
            if (i >= k - 1) {
                while (max_heap.top().second <= i - k) {
                    max_heap.pop();
                }
                answer.push_back(max_heap.top().first);
            }
        }
        return answer;
    }
};
