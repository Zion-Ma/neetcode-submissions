class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> lifo;
        for (string token : tokens) {
            if (token == "+") {
                int n1 = lifo.back();
                lifo.pop_back();
                int n2 = lifo.back();
                lifo.pop_back();
                lifo.emplace_back(n1 + n2);
            } else if (token == "*") {
                int n1 = lifo.back();
                lifo.pop_back();
                int n2 = lifo.back();
                lifo.pop_back();
                lifo.emplace_back(n1 * n2);
            } else if (token == "-") {
                int n1 = lifo.back();
                lifo.pop_back();
                int n2 = lifo.back();
                lifo.pop_back();
                lifo.emplace_back(n2 - n1);
            } else if (token == "/") {
                int n1 = lifo.back();
                lifo.pop_back();
                int n2 = lifo.back();
                lifo.pop_back();
                lifo.emplace_back(n2 / n1);
            } else {
                lifo.emplace_back(stoi(token));
            }
        }
        return lifo[0];
    }
};
