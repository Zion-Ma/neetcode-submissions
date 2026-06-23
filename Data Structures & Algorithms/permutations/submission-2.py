class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def perm(curr_list: list, curr_pool: list) -> None:
            if not curr_pool:
                ans.append(curr_list.copy())
                return
            for i in range(len(curr_pool)):
                curr_list.append(curr_pool[i])
                curr_pool.pop(i)
                perm(curr_list, curr_pool)
                val = curr_list.pop()
                curr_pool.insert(i, val)
            return
        perm([], nums.copy())
        return ans
