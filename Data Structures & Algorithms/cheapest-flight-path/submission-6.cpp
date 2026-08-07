class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<int> price(n, INT_MAX);
        price[src] = 0;
        for (int i = 0; i <= k; i++) {
            vector<int> tempPrice = price;
            for (const auto& f : flights) {
                int s = f[0], d = f[1], p = f[2];
                if (price[s] == INT_MAX) {continue;}
                tempPrice[d] = min(tempPrice[d], price[s] + p);
            }
            price = tempPrice;
        }
        return (price[dst] == INT_MAX ? -1 : price[dst]);
    }
};
