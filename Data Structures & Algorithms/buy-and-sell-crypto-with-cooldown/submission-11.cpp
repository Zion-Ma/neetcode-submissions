class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<vector<int>> dp((int)prices.size() + 2, vector<int>(2, 0));
        for (int i = (int)prices.size() - 1; i > -1; i--) {
            for (const int canbuy : {0, 1}) {
                int cooldown = dp[i + 1][canbuy];
                int profit = (
                    canbuy ?
                    dp[i + 1][0] - prices[i] :
                    dp[i + 2][1] + prices[i]
                );
                dp[i][canbuy] = max(cooldown, profit);
            }
        }
        return dp[0][1];
    }
};
