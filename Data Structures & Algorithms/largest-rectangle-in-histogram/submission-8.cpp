class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<pair<int, int>> s;
        int max_area = 0;
        heights.push_back(0);
        for (int i = 0; i < heights.size(); i++) {
            int start = i;
            while (!s.empty() and s.top().second >= heights[i]) {
                max_area = max(max_area, s.top().second * (i - s.top().first));
                start = s.top().first;
                s.pop();
            }
            s.push({start, heights[i]});
        }
        return max_area;
    }
};