class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def add(curr_list: list, curr_sum: int, curr_idx: int) -> None:
            if curr_sum == target:
                ans.append(curr_list.copy())
                return
            if curr_sum > target or curr_idx >= len(candidates):
                return 
            curr_list.append(candidates[curr_idx])
            add(curr_list, curr_sum + candidates[curr_idx], curr_idx + 1)
            curr_list.pop()
            while curr_idx + 1 < len(candidates) and candidates[curr_idx] == candidates[curr_idx + 1]:
                curr_idx += 1
            add(curr_list, curr_sum, curr_idx + 1)
            return
        add([], 0, 0)
        return ans
