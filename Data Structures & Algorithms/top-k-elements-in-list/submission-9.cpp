class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        priority_queue<pair<int, int>, vector<pair<int, int>>> heap;
        for (const auto& [key, value] : count) {
            heap.push({value, key});
        }
        vector<int> result;
        while (result.size() < k) {
            result.emplace_back(heap.top().second);
            heap.pop();
        }
        return result;
    }
};
