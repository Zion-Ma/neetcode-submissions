class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> lifo;
        for (string token : tokens) {
            if (token == "+") {
                int n1 = lifo.top();
                lifo.pop();
                int n2 = lifo.top();
                lifo.pop();
                lifo.push(n1 + n2);
            } else if (token == "*") {
                int n1 = lifo.top();
                lifo.pop();
                int n2 = lifo.top();
                lifo.pop();
                lifo.push(n1 * n2);
            } else if (token == "-") {
                int n1 = lifo.top();
                lifo.pop();
                int n2 = lifo.top();
                lifo.pop();
                lifo.push(n2 - n1);
            } else if (token == "/") {
                int n1 = lifo.top();
                lifo.pop();
                int n2 = lifo.top();
                lifo.pop();
                lifo.push(n2 / n1);
            } else {
                lifo.push(stoi(token));
            }
        }
        return lifo.top();
    }
};
