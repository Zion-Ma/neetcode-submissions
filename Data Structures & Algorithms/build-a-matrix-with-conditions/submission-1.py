class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        left_to_right = [[] for _ in range(k + 1)]
        top_to_down = [[] for _ in range(k + 1)]
        degree_h = [0 for i in range(k + 1)]
        degree_v = [0 for i in range(k + 1)]
        for above, below in rowConditions:
            top_to_down[above].append(below)
            degree_v[below] += 1
        for left, right in colConditions:
            left_to_right[left].append(right)
            degree_h[right] += 1
        order_h = self.findOrder(left_to_right, degree_h, k)
        if len(order_h) < k:
            return []
        order_v = self.findOrder(top_to_down, degree_v, k)
        if len(order_v) < k:
            return []
        pos_h = {num:pos for pos, num in enumerate(order_h)}
        pos_v = {num:pos for pos, num in enumerate(order_v)}
        res = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(1, k + 1):
            r, c = pos_v[i], pos_h[i]
            res[r][c] = i
        
        return res


    def findOrder(self, graph: list, degree: list, k: int) -> list:
        queue = deque([])
        order = []
        for i in range(1, k + 1):
            if degree[i] == 0:
                queue.append(i)
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for nei in graph[curr]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    queue.append(nei)
        return order

