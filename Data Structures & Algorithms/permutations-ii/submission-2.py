class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        idx = 0
        while idx < len(nums):
            new_res = []
            for curr in res:
                # curr = res.pop()
                for i in range(len(curr) + 1):
                    if i > 0 and curr[i - 1] == nums[idx]:
                        break
                    perm = curr.copy()
                    perm.insert(i, nums[idx])
                    new_res.append(perm)
            res = new_res
            idx += 1
        return res