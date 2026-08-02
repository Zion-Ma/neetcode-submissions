class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> freq;
        priority_queue<int> freq_heap;
        for (const char ch : tasks) {
            freq[ch]++;
        }
        for (const auto& [ch, f] : freq) {
            freq_heap.push(f);
        }
        int cycle = 0;
        while (!freq_heap.empty()) {
            int job_done = 0;
            vector<int> job_remain;
            while (!freq_heap.empty() and job_done < n + 1) {
                int curr = freq_heap.top();
                freq_heap.pop();
                curr--;
                if (curr > 0) {
                    job_remain.push_back(curr);
                }
                job_done++;
            }
            for (const int f : job_remain) {
                freq_heap.push(f);
            }
            cycle += (freq_heap.empty() ? job_done : n + 1);
        }
        return cycle;
    }
};
