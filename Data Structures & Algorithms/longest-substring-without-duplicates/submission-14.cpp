class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> record;
        int ans = 0;
        int start = 0;
        for (int i = 0; i < s.size(); i++) {
            if (record.find(s[i]) != record.end()) {
                start = max(record[s[i]] + 1, start);
            }
            record[s[i]] = i;
            ans = max(i - start + 1, ans);
        }
        return ans;
    }
};
