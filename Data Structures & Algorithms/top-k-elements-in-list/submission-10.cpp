class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (const int num : nums) {
            freq[num]++;
        }
        priority_queue<pair<int, int>> heap;
        for (const auto& [num, freq] : freq) {
            heap.push({freq, num});
        }
        vector<int> result;
        while (k > 0) {
            result.emplace_back(heap.top().second);
            heap.pop();
            k--;
        }
        return result;
    }
};
