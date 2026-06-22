"""
1. build parent and rank
2. for each node, find its root parent
3. if two connected nodes have the same parent, return false
4. compare two connected nodes by their parent's rank and merge
5. if any edge got false, return it
6. repeat 1-5
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [0 for _ in range(len(edges) + 1)]
        
        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j) -> bool:
            p, q = find(i), find(j)
            if p == q:
                return False
            if rank[p] > rank[q]:
                parent[q] = parent[p]
                rank[p] += rank[q]
            else:
                parent[p] = parent[q]
                rank[q] += rank[p]
            return True
        
        for x, y in edges:
            if not union(x, y):
                return [x, y]
