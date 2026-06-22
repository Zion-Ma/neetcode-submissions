class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for _ in range(n + 1)]
        log = 0
        for i in range(1, n + 1):
            if i == (2 ** log):
                ans[i] = 1
                log += 1
            else:
                ans[i] = 1 + ans[i - 2 ** (log - 1)]
        return ans

        
        