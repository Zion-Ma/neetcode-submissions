class Solution {
public:
    string minWindow(string s, string t) {
        if (t.size() == 0) {return "";}
        unordered_map<char, int> window;
        unordered_map<char, int> t_freq;
        int res_len = INT_MAX;
        int res_start = 0;
        for (const char c : t) {
            t_freq[c]++;
        }
        int have = 0, need = (int)t_freq.size();
        int l = 0;
        for (int r = 0; r < s.size(); r++) {
            char c = s[r];
            window[c]++;
            if (t_freq.count(c) && window[c] == t_freq[c]) {
                have++;
            }
            while (have == need) {
                int curr_len = r - l + 1;
                if (curr_len < res_len) {
                    res_len = curr_len;
                    res_start = l;
                }
                window[s[l]]--;
                if (t_freq.count(s[l]) && window[s[l]] < t_freq[s[l]]) {
                    have--;
                }
                l++;
            }
        }
        return res_len == INT_MAX ? "" : s.substr(res_start, res_len);
    }
};
