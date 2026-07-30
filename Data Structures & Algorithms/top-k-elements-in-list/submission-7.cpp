class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> records;
        for (int n : nums) {
            records[n]++;
        }
        vector<pair<int, int>> arr;
        for (const auto& p : records) {
            arr.emplace_back(p.second, p.first);
        }
        sort(arr.rbegin(), arr.rend());
        vector<int> res;
        for (int i = 0; i < k; i++) {
            res.emplace_back(arr[i].second);
        }
        return res;
    }
};
