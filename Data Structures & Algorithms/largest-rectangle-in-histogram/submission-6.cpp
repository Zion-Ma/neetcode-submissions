class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<pair<int, int>> s;
        int max_area = 0;
        int n = (int)heights.size();
        for (int i = 0; i < n; i++) {
            if (s.empty() or s.top().second < heights[i]) {
                s.push({i, heights[i]});
            } else {
                int extendable = 0;
                while (!s.empty() and s.top().second >= heights[i]) {
                    max_area = max(max_area, s.top().second * (i - s.top().first));
                    extendable = s.top().first;
                    s.pop();
                }
                s.push({extendable, heights[i]});
            }
        }
        while (!s.empty()) {
            max_area = max(max_area, s.top().second * (n - s.top().first));
            s.pop();
        }
        return max_area;
    }
};
