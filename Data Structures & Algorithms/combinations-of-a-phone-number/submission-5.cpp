class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        if (digits.empty()) {return result;}
        unordered_map<char, string> record;
        string curr;
        vector<string> digitToChar = {"", "", "abc", "def", "ghi", "jkl",
                                  "mno", "qprs", "tuv", "wxyz"};
        backtrack(0, curr, result, digitToChar, digits);
        return result;
    }
    void backtrack(
        int i, string& curr, vector<string>& result, 
        const vector<string>& digitToChar, const string& digits
    ) {
        if (i == digits.size()) {
            result.push_back(curr);
            return;
        }
        for (const char c : digitToChar[digits[i] - '0']) {
            curr += c;
            backtrack(i + 1, curr, result, digitToChar, digits);
            curr.pop_back();
        }
    }
};
