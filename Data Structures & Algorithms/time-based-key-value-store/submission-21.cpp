class TimeMap {
    unordered_map<string, vector<pair<string, int>>> record;
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        record[key].push_back({value, timestamp});
    }
    
    string get(string key, int timestamp) {
        if (record.find(key) == record.end()) {
            return "";
        }
        vector<int> time_list;
        for (const auto& [value, t] : record[key]) {
            time_list.push_back(t);
        }
        int left = 0, right = time_list.size() - 1;
        int at = 0;
        string res = "";
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (time_list[mid] == timestamp) {
                return record[key][mid].first;
            }
            if (time_list[mid] > timestamp) {
                right = mid - 1;
            } else {
                res = record[key][mid].first;
                left = mid + 1;
            }
        }
        return res;
    }
};
