class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i: int, curr_list: list) -> None:
            if len(curr_list) == k:
                ans.append(curr_list.copy())
                return
            if i > n or (n - i + 1) < (k - len(curr_list)):
                return
            curr_list.append(i)
            backtrack(i + 1, curr_list)
            curr_list.pop()
            backtrack(i + 1, curr_list)
            return
        
        ans = []
        backtrack(1, [])
        return ans