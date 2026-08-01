class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        // std::make_heap(stones.begin(), stones.end());
        priority_queue<int> heap;
        for (const int s : stones) {
            heap.push(s);
        }
        while ((int)heap.size() > 1) {
            int s1 = heap.top();
            heap.pop();
            int s2 = heap.top();
            heap.pop();
            int remain = abs(s1 - s2);
            if (remain) {
                heap.push(remain);
            }
        }
        return heap.empty() ? 0 : heap.top();
    }
};
