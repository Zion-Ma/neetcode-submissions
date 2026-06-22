class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def traverse(curr_list: list, curr_sum: int, i: int) -> None:
            if curr_sum == target:
                result.append(curr_list.copy())
                return
            if i == len(nums) or curr_sum > target:
                return
            curr_list.append(nums[i])
            traverse(curr_list, curr_sum + nums[i], i)
            curr_list.pop()
            traverse(curr_list, curr_sum, i + 1)
        traverse([], 0, 0)
        return result
                