class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s2.size() < s1.size()) return false;
        int n1 = s1.size();
        int n2 = s2.size();
        vector<int> r1(26, 0);
        vector<int> r2(26, 0);
        int match = 0;
        int start = 0;
        for (int i = 0; i < n1; i++) {
            r1[s1[i] - 'a']++;
            r2[s2[i] - 'a']++;
        }
        for (int i = 0; i < 26; i++) {
            if (r1[i] == r2[i]) match++;
        }
        for (int i = n1; i < n2; i++) {
            if (match == 26) {
                return true;
            }
            char right_char = s2[i];
            if (r2[right_char - 'a'] == r1[right_char - 'a']) {match--;} 
            else if (r2[right_char - 'a'] == r1[right_char - 'a'] - 1) {match++;}
            r2[right_char - 'a']++;
            char left_char = s2[start];
            if (r2[left_char - 'a'] == r1[left_char - 'a']) {match--;} 
            else if (r2[left_char - 'a'] == r1[left_char - 'a'] + 1) {match++;}
            r2[left_char - 'a']--;
            start++;
        }
        return match == 26;
    }
};
