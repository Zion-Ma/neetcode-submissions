class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> records;
        for (const auto& s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            records[key].emplace_back(s);
        }
        vector<vector<string>> result;
        for (const auto& [key, value] : records) {
            result.emplace_back(move(value));
        }
        return result;
    }
};
