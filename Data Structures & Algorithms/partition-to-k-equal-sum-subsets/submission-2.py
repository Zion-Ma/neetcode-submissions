class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        target = total // k
        if total % k != 0:
            return False
        nums.sort()
        def backtrack(i: int, curr_status: list) -> bool:
            if i == len(nums):
                return True
            seen = set()
            for j in range(len(curr_status)):
                if curr_status[j] in seen or curr_status[j] == target or curr_status[j] + nums[i] > target:
                    continue
                seen.add(curr_status[j])
                curr_status[j] += nums[i]
                if backtrack(i + 1, curr_status):
                    return True
                curr_status[j] -= nums[i]
            return False
        curr_status = [0 for _ in range(k)]
        return backtrack(0, curr_status)
