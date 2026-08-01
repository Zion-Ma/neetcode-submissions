class KthLargest {
public:
    int limit;
    priority_queue<int, vector<int>, greater<int>> min_heap;
    KthLargest(int k, vector<int>& nums) {
        limit = k;
        for (const int n : nums) {
            min_heap.push(n);
        }
        while ((int)min_heap.size() > limit) {
            min_heap.pop();
        }
    }
    
    int add(int val) {
        min_heap.push(val);
        if ((int)min_heap.size() > limit) {
            min_heap.pop();
        }
        return min_heap.top();
    }
};
