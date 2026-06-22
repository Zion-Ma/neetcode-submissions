class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for i, n in enumerate(nums):
            new = []
            for p in perms:
                for j in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(j, n)
                    new.append(p_copy)
            perms = new
            # res += perms
        return perms