class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, curr_list, curr_sum):
            if curr_sum == target:
                res.append(curr_list.copy())
                return
            if i == len(candidates) or curr_sum > target:
                return
            curr_list.append(candidates[i])
            dfs(i + 1, curr_list, curr_sum + candidates[i])
            curr_list.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr_list, curr_sum)
        dfs(0, [], 0)
        return res