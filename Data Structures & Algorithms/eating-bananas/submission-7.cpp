class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int max_pile = *max_element(piles.begin(), piles.end());
        int start = 1, end = max_pile;
        int ans = max_pile;
        while (start < end) {
            int rate = start + (end - start) / 2;
            int hour = 0;
            for (const int p : piles) {
                hour += ((p + rate - 1) / rate);
            }
            if (hour > h) {
                start = rate + 1;
            } else {
                ans = min(ans, rate);
                end = rate;
            }
        }
        return ans;
    }
};
