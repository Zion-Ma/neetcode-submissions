class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<bool>> pal;
        vector<vector<string>> result;
        vector<string> part;
        int n = s.size();
        pal.assign(n, vector<bool>(n, false));
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1])){
                    pal[i][j] = true;
                }
            }
        }
        backtrack(0, s, pal, result, part);
        return result;
    }
    void backtrack(int i, const string& s, const vector<vector<bool>>& pal, vector<vector<string>>& result, vector<string>& part) {
        int n = s.size();
        if (i == n) {
            result.push_back(part);
            return;
        }
        for (int j = i; j < n; j++) {
            if (!pal[i][j]) {continue;}
            part.push_back(s.substr(i, j - i + 1));
            backtrack(j + 1, s, pal, result, part);
            part.pop_back();
        }
    }
};
