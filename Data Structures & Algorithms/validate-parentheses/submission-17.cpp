class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> record = {{']', '['}, {')', '('}, {'}', '{'}};
        vector<char> lifo;
        for (const char mark : s) {
            if (record.find(mark) == record.end()) {
                lifo.emplace_back(mark);
            } else {
                if (lifo.empty() or lifo.back() != record[mark]) {return false;}
                lifo.pop_back();
            }
        }
        return lifo.empty();
    }
};
