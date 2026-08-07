// vector (0 ... amount)
// vector[i] = max(vector[i - current coin] + 1)

class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<int> dp(amount + 1, 0);
        dp[0] = 1;
        sort(coins.begin(), coins.end());
        for (const int c : coins) {
            vector<int> new_dp = dp;
            for (int a = 1; a <= amount; a++) {
                int diff = a - c;
                if (diff >= 0) {
                    new_dp[a] += new_dp[diff];
                }
            }
            dp = new_dp;
        }
        return dp[amount];
    }
};
