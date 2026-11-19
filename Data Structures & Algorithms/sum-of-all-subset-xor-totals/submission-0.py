class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(curr: int, idx: int) -> None:
            if idx == len(nums):
                self.ans += curr
                return
            dfs(curr, idx + 1)
            dfs(curr ^ nums[idx], idx + 1)
            return
        
        self.ans = 0
        dfs(0, 0)
        return self.ans
            
