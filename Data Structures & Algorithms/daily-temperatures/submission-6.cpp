class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> result(temperatures.size(), 0);
        stack<int> lifo;
        lifo.push(0);
        for (int i = 1; i < temperatures.size(); i++) {
            while (!lifo.empty() and temperatures[lifo.top()] < temperatures[i]) {
                result[lifo.top()] = i - lifo.top();
                lifo.pop();
            }
            lifo.push(i);
        }
        return result;
    }
};
