"""
get the smallest maximum of each path
1. initialize a minHeap with the top-left value
2. pop from the heap and traverse the node's neighbors
3. push new node with the value of (max-val of the previous path, current)
4. return the max-val when we reach the bottom-right
"""

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [(grid[0][0], (0, 0))]
        visited = set()
        visited.add((0, 0))
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while minHeap:
            t, (r, c) = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1:
                return t
            for nr, nc in direc:
                i, j = r + nr, c + nc
                if 0 <= i < N and 0 <= j < N and (i, j) not in visited:
                    heapq.heappush(minHeap, (max(t, grid[i][j]), (i, j)))
                    visited.add((i, j))
    

