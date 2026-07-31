class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        stack<double> lifo;
        vector<pair<int, double>> time;
        for (int i = 0; i < speed.size(); i++) {
            double t = speed[i] != 0 ? (double)(target - position[i]) / speed[i] : 0;
            time.emplace_back(position[i], t);
        }
        sort(time.rbegin(), time.rend());

        for (auto& [pos, t] : time) {
            if (lifo.empty()) {
                lifo.push(t);
            } else if (lifo.top() < t) {
                lifo.push(t);
            }
        }
        return lifo.size();
    }
};
