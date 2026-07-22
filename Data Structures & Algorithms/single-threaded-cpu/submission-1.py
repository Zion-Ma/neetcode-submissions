class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key = lambda x:x[0])
        idx, time = 0, 0
        heap, ans = [], []
        while heap or idx < len(tasks):
            while idx < len(tasks) and tasks[idx][0] <= time:
                heapq.heappush(heap, (tasks[idx][1], tasks[idx][2]))
                idx += 1
            if not heap:
                time = tasks[idx][0]
            else:
                proc, curr_idx = heapq.heappop(heap)
                time += proc
                ans.append(curr_idx)
        return ans
            