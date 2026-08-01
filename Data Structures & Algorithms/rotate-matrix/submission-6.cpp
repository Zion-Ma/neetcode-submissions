class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        std::reverse(matrix.begin(), matrix.end());
        int n = (int)matrix.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp1 = matrix[i][j], temp2 = matrix[j][i];
                matrix[i][j] = temp2;
                matrix[j][i] = temp1;
            }
        }
    }
};
