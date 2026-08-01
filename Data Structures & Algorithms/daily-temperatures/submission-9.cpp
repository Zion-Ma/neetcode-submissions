class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> lifo;
        vector<int> result(temperatures.size(), 0);
        for (int i = 0; i < temperatures.size(); i++) {
            while (!lifo.empty() and temperatures[lifo.top()] < temperatures[i]) {
                result[lifo.top()] = i - lifo.top();
                lifo.pop();
            }
            lifo.push(i);
        }
        return result;
    }
};
