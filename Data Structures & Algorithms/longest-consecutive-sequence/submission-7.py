class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = dict()
        ans = 0
        for num in nums:
            if num in mp:
                continue
            length = mp.get(num - 1, 0) + mp.get(num + 1, 0) + 1
            mp[num] = length
            mp[num - mp.get(num - 1, 0)] = length
            mp[num + mp.get(num + 1, 0)] = length
            ans = max(ans, length)
        return ans
