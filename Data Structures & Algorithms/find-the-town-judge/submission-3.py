class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustBy = defaultdict(int)
        for trustor, trustee in trust:
            trustBy[trustee] += 1
            trustBy[trustor] -= 1
        for i in range(1, n + 1):
            if trustBy[i] == n - 1:
                return i
        return -1