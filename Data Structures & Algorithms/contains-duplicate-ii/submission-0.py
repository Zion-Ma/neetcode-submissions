class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for r in range(len(nums)):
            if nums[r] in window:
                return True
            window.add(nums[r])
            if len(window) == k + 1:
                window.remove(nums[r - k])
        return False