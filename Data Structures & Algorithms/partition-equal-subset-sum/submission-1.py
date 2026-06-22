class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        half = s // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            nextDP = dp.copy()
            for t in dp:
                curr = t + nums[i]
                if curr == half:
                    return True
                nextDP.add(curr)
            dp = nextDP
        return False
            