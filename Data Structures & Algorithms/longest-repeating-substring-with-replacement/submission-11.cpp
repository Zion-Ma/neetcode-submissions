class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> freq;
        char max_key = '.';
        freq[max_key] = 0;
        int start = 0;
        int ans = 0;
        for (int i = 0; i < s.size(); i++) {
            char curr_key = s[i];
            freq[curr_key]++;
            if (freq[curr_key] > freq[max_key]) {
                max_key = curr_key;
            }
            if ((i - start + 1 - freq[max_key]) > k) {
                freq[s[start]]--;
                start += 1;
            }
            ans = std::max(ans, i - start + 1);
        }
        return ans;
    }
};
