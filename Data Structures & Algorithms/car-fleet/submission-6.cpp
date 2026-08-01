class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, double>> time;
        stack<double> fleet;
        for (int i = 0; i < position.size(); i++) {
            double t = speed[i] != 0 ? (double)(target - position[i]) / speed[i] : INFINITY;
            time.push_back({position[i], t});
        }
        sort(time.rbegin(), time.rend());
        for (const auto& [pos, t] : time) {
            if (fleet.empty()) {
                fleet.push(t);
            } else if (!fleet.empty() and fleet.top() < t) {
                fleet.push(t);
            }
        }
        return (int)fleet.size();
    }
};
