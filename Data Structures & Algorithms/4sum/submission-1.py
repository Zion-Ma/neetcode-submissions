class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                sub_target = target - (nums[i] + nums[j])
                l, r = j + 1, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s > sub_target:
                        r -= 1
                    elif s < sub_target:
                        l += 1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        l += 1
                        r -= 1
        return ans
