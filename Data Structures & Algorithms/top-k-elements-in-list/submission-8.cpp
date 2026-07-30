class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (const int num : nums) {
            freq[num]++;
        }
        vector<pair<int, int>> record;
        for (const auto& [key, value] : freq) {
            record.emplace_back(value, key);
        }
        sort(record.rbegin(), record.rend());
        vector<int> result;
        for (int i = 0; i < k; i++) {
            result.emplace_back(record[i].second);
        }
        return result;
    }
};
