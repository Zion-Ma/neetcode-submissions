class Solution {
public:

    string encode(vector<string>& strs) {
        string result = "";
        for (const string& s : strs) {
            result += std::format("{}#{}", to_string(s.size()), s);
        }
        return result;
    }

    vector<string> decode(string s) {
        size_t i = 0;
        vector<string> result;
        while (i < s.size()) {
            size_t j = i;
            while (s[j] != '#') {
                j++;
            }
            size_t length = stoi(s.substr(i, j - i));
            result.emplace_back(s.substr(j + 1, length));
            i = j + 1 + length;
        }
        return result;
    }
};
