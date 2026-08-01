class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> record = {{']', '['}, {')', '('}, {'}', '{'}};
        stack<char> lifo;
        for (const char mark : s) {
            if (record.find(mark) == record.end()) {
                lifo.push(mark);
            } else {
                if (lifo.empty() or lifo.top() != record[mark]) {return false;}
                lifo.pop();
            }
        }
        return lifo.empty();
    }
};
