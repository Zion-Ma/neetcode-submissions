class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        if (digits.empty()) {return result;}
        unordered_map<char, string> record;
        string curr;
        for (int i = 2; i <= 6; i++) {
            for (int j = 0; j < 3; j++) {
                char key = i + '0';
                record[key] += (((i - 2) * 3 + j) + 'a');
            }
        }
        record['7'] = "pqrs";
        record['8'] = "tuv";
        record['9'] = "wxyz";
        backtrack(0, curr, result, record, digits);
        return result;
    }
    void backtrack(
        int i, string& curr, vector<string>& result, 
        const unordered_map<char, string>& record, const string& digits
    ) {
        if (i == digits.size()) {
            result.push_back(curr);
            return;
        }
        for (const char c : record.at(digits[i])) {
            curr += c;
            backtrack(i + 1, curr, result, record, digits);
            curr.pop_back();
        }
    }
};
