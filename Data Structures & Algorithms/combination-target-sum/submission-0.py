class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def DFS(curr: list, total: int, idx: int):
            if total == target:
                sol.append(curr)
                return
            if idx >= cand_len or total > target:
                return
            DFS(curr + [nums[idx]], total + nums[idx], idx)
            DFS(curr, total, idx + 1)
        sol = []
        cand_len = len(nums)
        DFS([], 0, 0)
        return sol
        