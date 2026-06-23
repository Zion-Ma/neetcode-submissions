class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def add(curr_list: int, curr_idx: int, curr_sum: int) -> None:
            if curr_idx >= len(nums) or curr_sum > target:
                return 
            if curr_sum == target:
                ans.append(curr_list.copy())
                return 
            add(curr_list, curr_idx + 1, curr_sum)
            curr_list.append(nums[curr_idx])
            add(curr_list, curr_idx, curr_sum + nums[curr_idx])
            curr_list.pop()
            return
        add([], 0, 0)
        return ans
