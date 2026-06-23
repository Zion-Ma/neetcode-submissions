class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def select(curr_list: list, i: int) -> None:
            if i > len(nums) - 1:
                ans.append(curr_list.copy())
                return
            curr_list.append(nums[i])
            select(curr_list, i + 1)
            curr_list.pop()
            select(curr_list, i + 1)
            return
        select([], 0)
        return ans