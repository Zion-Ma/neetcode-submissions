class Solution {
public:

    string encode(vector<string>& strs) {
        string result = "";
        for (const string str : strs) {
            size_t length = str.size();
            result += (to_string(length) + "#" + str);
        }
        return result;
    }

    vector<string> decode(string s) {
        vector<string> result;
        size_t i = 0;
        while (i < s.size()) {
            size_t j = i;
            while (s[j] != '#') {
                j++;
            }
            size_t length = stoi(s.substr(i, j - i));
            result.emplace_back(s.substr(j + 1, length));
            i = j + length + 1;
        }
        return result;
    }
};
