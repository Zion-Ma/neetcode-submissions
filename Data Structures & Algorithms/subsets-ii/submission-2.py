class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def select(curr_list: list, curr_idx: int) -> None:
            if curr_idx == len(nums):
                ans.append(curr_list.copy())
                return
            curr_list.append(nums[curr_idx])
            select(curr_list, curr_idx + 1)
            curr_list.pop()
            while curr_idx < len(nums) - 1 and nums[curr_idx] == nums[curr_idx + 1]:
                curr_idx += 1
            select(curr_list, curr_idx + 1)
            return
        select([], 0)
        return ans
                
            