class Solution {
public:
    vector<string> digitToChar = {"", "", "abc", "def", "ghi", "jkl",
                                  "mno", "qprs", "tuv", "wxyz"};
    vector<string> result;
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) {return result;}
        unordered_map<char, string> record;
        string curr;
        backtrack(0, curr, digits);
        return result;
    }
    void backtrack(int i, string& curr, const string& digits) {
        if (i == digits.size()) {
            result.push_back(curr);
            return;
        }
        for (const char c : digitToChar[digits[i] - '0']) {
            curr += c;
            backtrack(i + 1, curr, digits);
            curr.pop_back();
        }
    }
};
