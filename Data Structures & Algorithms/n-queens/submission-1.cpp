class Solution {
public:
    vector<vector<string>> result;
    vector<vector<char>> curr;
    unordered_set<int> col;
    unordered_set<int> pos_diag;
    unordered_set<int> neg_diag;
    vector<vector<string>> solveNQueens(int n) {
        curr.assign(n, vector<char>(n, '.'));
        backtrack(0, n);
        return result;
    }
    void backtrack(int r, int n) {
        if (r == n) {
            vector<string> ans;
            for (int j = 0; j < n; j++) {
                string s(curr[j].begin(), curr[j].end());
                ans.push_back(s);
            }
            result.push_back(ans);
            return;
        }
        for (int c = 0; c < n; c++) {
            if (col.count(c) or pos_diag.count(r + c) or neg_diag.count(r - c)){
                continue;
            }
            curr[r][c] = 'Q';
            col.insert(c);
            pos_diag.insert(r + c);
            neg_diag.insert(r - c);
            backtrack(r + 1, n);
            curr[r][c] = '.';
            col.erase(c);
            pos_diag.erase(r + c);
            neg_diag.erase(r - c);
        }
    }
};
