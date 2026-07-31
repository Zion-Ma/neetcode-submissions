class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int lowest = prices[0];
        for (const int p : prices) {
            profit = std::max(profit, p - lowest);
            lowest = std::min(lowest, p);
        }
        return profit;
    }
};
