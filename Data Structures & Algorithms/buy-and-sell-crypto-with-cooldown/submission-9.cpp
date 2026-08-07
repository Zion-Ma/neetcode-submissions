class Solution {
public:
    unordered_map<int, unordered_map<int, int>> dp;
    vector<int> prices_;
    int maxProfit(vector<int>& prices) {
        prices_ = prices;
        return dfs(0, 1);
    }
    int dfs(int i, int canbuy) {
        if (i >= prices_.size()) {return 0;}
        if (dp.count(i) and dp[i].count(canbuy)) {
            return dp[i][canbuy];
        }
        int cooldown = dfs(i + 1, canbuy);
        int profit;
        // 1
        if (canbuy) {
            profit = dfs(i + 1, 0) - prices_[i];
        } else {
            profit = dfs(i + 2, 1) + prices_[i];
        }
        dp[i][canbuy] = max(cooldown, profit);
        return dp[i][canbuy];
    }
};
