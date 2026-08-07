class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> dp1(2, 0);
        vector<int> dp2(2, 0);
        for (int i = (int)prices.size() - 1; i > -1; i--) {
            vector<int> new_dp(2, 0);
            for (const int canbuy : {0, 1}) {
                int cooldown = dp1[canbuy];
                int profit = (
                    canbuy ?
                    dp1[0] - prices[i] :
                    dp2[1] + prices[i]
                );
                new_dp[canbuy] = max(cooldown, profit);
            }
            dp2 = dp1;
            dp1 = new_dp;
        }
        return dp1[1];
    }
};
