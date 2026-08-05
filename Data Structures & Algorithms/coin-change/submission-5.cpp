class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> record(amount + 1, INT_MAX);
        record[0] = 0;
        sort(coins.begin(), coins.end());
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                int diff = i - coin;
                if (diff >= 0 and record[diff] != INT_MAX) {
                    record[i] = min(record[i], 1 + record[diff]);
                }
            }
        }
        return (record.back() == INT_MAX ? -1 : record.back());
    }
};
