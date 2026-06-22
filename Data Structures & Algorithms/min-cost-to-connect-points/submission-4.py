"""
1. initialize distance array, dist, with all element as inf
2. pick one element and relax it to 0 and begin with it
3. for each unvisited node j, calculate the dist with the current node
4. if dist[j] > edge(i, j), dist[j] = edge(i, j)
5. find the minimum in dist and set it to the next node
6. add result with dist[j]
7. repeat 3 - 5 for all nodes
8. retur result
"""

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = [float("inf")] * len(points)
        visited = [False] * len(points)
        # dist[0] = 0
        length = 0
        node = 0
        traversed = 0
        while traversed < len(points) - 1:
            visited[node] = True
            next_node = -1
            for j in range(len(points)):
                if visited[j]:
                    continue
                curr_dist = abs(points[node][0] - points[j][0]) + abs(points[node][1] - points[j][1])
                dist[j] = min(dist[j], curr_dist)
                if next_node == -1 or dist[j] < dist[next_node]:
                    next_node = j
            length += dist[next_node]
            node = next_node
            traversed += 1
        return length
        