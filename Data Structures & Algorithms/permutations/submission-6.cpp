class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        result.push_back({});
        for (const int n : nums) {
            vector<vector<int>> new_result;
            for (const auto& r : result) {
                for (int i = 0; i <= r.size(); i++) {
                    vector<int> curr = r;
                    curr.insert(curr.begin() + i, n);
                    new_result.push_back(curr);
                }
            }
            result = new_result;
        }
        return result;
    }
};
