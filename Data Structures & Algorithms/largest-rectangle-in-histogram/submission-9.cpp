class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<pair<int, int>> s;
        int max_area = 0;
        heights.push_back(0);
        int n = (int)heights.size();
        for (int i = 0; i < n; i++) {
            int extendable = i;
            while (!s.empty() and s.top().second >= heights[i]) {
                max_area = max(max_area, s.top().second * (i - s.top().first));
                extendable = s.top().first;
                s.pop();
            }
            s.push({extendable, heights[i]});
            // max_area = max(max_area, s.top().second * (n - s.top().first));
        }
        // while (!s.empty()) {
        //     max_area = max(max_area, s.top().second * (n - s.top().first));
        //     s.pop();
        // }
        return max_area;
    }
};
