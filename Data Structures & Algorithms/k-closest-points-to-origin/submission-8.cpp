class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<double, int>, vector<pair<double, int>>, greater<pair<double, int>>> heap;
        vector<vector<int>> result;
        for (int i = 0; i < points.size(); i++) {
            double dist = sqrt(std::pow(points[i][0], 2) + std::pow(points[i][1], 2));
            cout<<dist<<' ';
            heap.push({dist, i});
        }
        cout<<'\n';
        while (k > 0) {
            pair<double, int> top = heap.top();
            std::cout<<top.second<<' ';
            vector<int> point = {points[top.second][0], points[top.second][1]};
            result.push_back(point);
            heap.pop();
            k--;
        }
        return result;
    }
};
