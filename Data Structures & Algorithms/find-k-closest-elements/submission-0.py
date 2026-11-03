class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dist = [abs(x - num) for num in arr]
        running_sum = 0
        global_min = float("inf")
        end = 0
        for i, d in enumerate(dist):
            running_sum += d
            if i < k - 1:
                continue
            if running_sum < global_min:
                global_min = running_sum
                end = i
            running_sum -= dist[i - k + 1]
        return arr[end - k + 1:end + 1]