class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" or num2 == "0") {
            return "0";
        }
        int m = (int)num1.size(), n = (int)num2.size();
        vector<int> result(m + n, 0);
        for (int i = m - 1; i > -1; i--){
            for (int j = n - 1; j > -1; j--) {
                int n1 = num1[i] - '0';
                int n2 = num2[j] - '0';
                int curr_res = n1 * n2 + result[i + j + 1];
                int val = curr_res % 10;
                int carry = curr_res / 10;
                result[i + j + 1] = val;
                result[i + j] += carry;
            }
        }
        string ans;
        int curr_idx = 0;
        while (curr_idx < m + n and result[curr_idx] == 0) {
            curr_idx++;
        }
        while (curr_idx < m + n) {
            ans += (result[curr_idx] + '0');
            curr_idx++;
        }
        return ans;
    }
};
