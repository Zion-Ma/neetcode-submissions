class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        res = [[]]
        idx = 0
        for num in nums:
            new_res = []
            for curr in res:
                for i in range(len(curr) + 1):
                    perm = curr[:i] + [num] + curr[i:]
                    new_res.append(perm)
                    if i < len(curr) and curr[i] == num:
                        break
            res = new_res
        return res