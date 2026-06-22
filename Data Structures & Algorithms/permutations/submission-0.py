class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr, remain):
            if not remain:
                res.append(curr.copy())
            for i in range(len(remain)):
                curr.append(remain[i])
                temp = remain[i]
                remain.pop(i)
                dfs(curr, remain)
                curr.pop()
                remain.insert(i, temp)
        dfs([], nums.copy())
        return res