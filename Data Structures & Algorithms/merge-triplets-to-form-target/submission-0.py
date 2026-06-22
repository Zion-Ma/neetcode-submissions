class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = [-1, -1, -1]
        for i in range(len(triplets)):
            if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                ans[0] = max(ans[0], triplets[i][0])
                ans[1] = max(ans[1], triplets[i][1])
                ans[2] = max(ans[2], triplets[i][2])
                if ans == target:
                    return True
        return False