class Solution {
public:
    unordered_map<int, unordered_map<int, int>> dp;
    int maxProfit(vector<int>& prices) {
        return dfs(0, 1, prices);
    }
    int dfs(int i, int canbuy, vector<int>& prices) {
        if (i >= prices.size()) {return 0;}
        if (dp.count(i) and dp[i].count(canbuy)) {
            return dp[i][canbuy];
        }
        int cooldown = dfs(i + 1, canbuy, prices);
        int profit;
        // 1
        if (canbuy) {
            profit = dfs(i + 1, 0, prices) - prices[i];
        } else {
            profit = dfs(i + 2, 1, prices) + prices[i];
        }
        dp[i][canbuy] = max(cooldown, profit);
        return dp[i][canbuy];
    }
};
