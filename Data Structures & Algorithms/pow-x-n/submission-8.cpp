class Solution {
public:
    double myPow(double x, int n) {
        long m = n;
        if (m < 0) {
            x = 1 / x;
            m = -m;
        }
        return helper(x, m);
    }
private:
    double helper(double x, long m) {
        if (m == 0) {return 1.0;}
        double half = helper(x, m / 2);
        return m % 2 ? half * half * x : half * half;
    }
};
