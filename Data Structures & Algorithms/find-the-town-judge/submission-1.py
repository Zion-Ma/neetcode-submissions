class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustBy = [0 for _ in range(n + 1)]
        trustOther = [0 for _ in range(n + 1)]
        for trustor, trustee in trust:
            trustBy[trustee] += 1
            trustOther[trustor] += 1
        for t in range(1, n + 1):
            if trustBy[t] == n - 1 and trustOther[t] == 0:
                return t
        return -1
        