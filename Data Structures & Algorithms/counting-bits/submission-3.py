class Solution:
    def countBits(self, n: int) -> List[int]:
        twos = 2
        dp = [0]
        for i in range(1, n + 1):
            if i < twos:
                dp.append(1 + dp[i - twos // 2])
            else:
                dp.append(1)
                twos *= 2
        return dp
        