class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def traverse(curr_list: list, i: int) -> None:
            if i >= len(nums):
                result.append(curr_list)
                return
            traverse(curr_list, i + 1)
            traverse(curr_list + [nums[i]], i + 1)
        traverse([], 0)
        return result