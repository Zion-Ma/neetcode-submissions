class TimeMap {
public:
    unordered_map<string, vector<pair<string, int>>> record;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        record[key].push_back({value, timestamp});
    }
    
    string get(string key, int timestamp) {
        if (record.find(key) == record.end()) {
            return "";
        }
        string ans;
        vector<int> time_list;
        for (const auto& [value, t] : record[key]) {
            time_list.push_back(t);
        }
        int left = 0, right = time_list.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (time_list[mid] > timestamp) {
                right = mid - 1;
            } else {
                ans = record[key][mid].first;
                left = mid + 1;
            }
        }
        return ans;
    }
};
