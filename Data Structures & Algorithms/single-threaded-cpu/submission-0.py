class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda x:x[0])
        ans, pq = [], []
        time, i = 0, 0
        while pq or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(pq, (tasks[i][1], tasks[i][2]))
                i += 1
            if not pq:
                time = tasks[i][0]
            else:
                proc, idx = heapq.heappop(pq)
                time += proc
                ans.append(idx)
        return ans