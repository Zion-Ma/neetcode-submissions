class Solution {
public:
    vector<string> results;
    vector<string> generateParenthesis(int n) {
        string curr = "(";
        dfs(1, 0, n, curr);
        return results;
    }
    void dfs(int o, int c, const int n, string& curr) {
        if (c > o or ((c == n) and (o < n))) {return;}
        if (o + c == 2 * n) {
            if (o == c) {
                results.push_back(curr);
            }
            return;
        }
        curr += '(';
        dfs(o + 1, c, n, curr);
        curr.pop_back();
        curr += ')';
        dfs(o, c + 1, n, curr);
        curr.pop_back();
        return;
    }
};
