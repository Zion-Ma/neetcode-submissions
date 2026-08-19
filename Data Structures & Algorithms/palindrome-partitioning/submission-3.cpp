class Solution {
public:
    vector<vector<string>> partition(string s) {
        int n = (int)s.size();
        vector<vector<bool>> pal(n, vector<bool>(n, false));
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1])) {
                    pal[i][j] = true;
                }
            }
        }
        vector<vector<string>> ans;
        vector<string> part;
        dfs(0, s, pal, part, ans);
        return ans;
    }
    void dfs(int i, const string& s, const vector<vector<bool>>& pal, vector<string>& part, vector<vector<string>>& ans) {
        int n = (int)s.size();
        if (i == n) {
            ans.push_back(part);
            return;
        }
        for (int j = i; j < n; j++) {
            if (!pal[i][j]) {continue;}
            part.push_back(s.substr(i, j - i + 1));
            dfs(j + 1, s, pal, part, ans);
            part.pop_back();
        }
    }
};
