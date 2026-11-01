class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key = lambda task : task[0])
        idx = 0
        minProcTime = []
        curr_end = 0
        res = []
        while idx < len(tasks):
            while idx < len(tasks) and curr_end >= tasks[idx][0]:
                heapq.heappush(minProcTime, (tasks[idx][1], tasks[idx][2]))
                idx += 1
            if minProcTime:
                time, i = heapq.heappop(minProcTime)
                curr_end += time
                res.append(i)
            else:
                curr_end = tasks[idx][0]
        while minProcTime:
            _, i = heapq.heappop(minProcTime)
            res.append(i)
        return res
                
