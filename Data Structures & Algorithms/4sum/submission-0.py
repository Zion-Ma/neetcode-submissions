class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        ans = []
        seen_outer = set()
        nums.sort()
        for i in range(len(nums)):
            if nums[i] in seen_outer:
                continue
            seen_inner = set()
            for j in range(i + 1, len(nums)):
                if nums[j] in seen_inner:
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
                seen_inner.add(nums[j])
            seen_outer.add(nums[i])
        return ans
