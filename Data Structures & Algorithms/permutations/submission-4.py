class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for i, n in enumerate(nums):
            new = []
            for p in perms:
                for j in range(len(p) + 1):
                    p_new = p.copy()
                    p_new.insert(j, n)
                    new.append(p_new)
            perms = new
        return perms