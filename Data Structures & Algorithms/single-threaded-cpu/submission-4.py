class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        order = sorted(range(len(tasks)), key = lambda i : tasks[i][0])
        idx = 0
        curr_end = 0
        minProcTime = []
        res = []
        while idx < len(tasks) or minProcTime:
            while idx < len(order) and curr_end >= tasks[order[idx]][0]:
                heapq.heappush(minProcTime, (tasks[order[idx]][1], order[idx]))
                idx += 1
            if minProcTime:
                time, i = heapq.heappop(minProcTime)
                curr_end += time
                res.append(i)
            else:
                curr_end = tasks[order[idx]][0]
        return res
                
