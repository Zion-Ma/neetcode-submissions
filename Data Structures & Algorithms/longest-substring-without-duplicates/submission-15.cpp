class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> pos;
        int ans = 0;
        int start = 0;
        for (int i = 0; i < s.size(); i++){
            if (pos.find(s[i]) != pos.end()) {
                start = max(start, pos[s[i]] + 1);
            }
            pos[s[i]] = i;
            ans = max(ans, i - start + 1);
        }
        return ans;
    }
};
