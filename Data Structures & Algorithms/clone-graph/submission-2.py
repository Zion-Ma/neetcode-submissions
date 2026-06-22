"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
1. build a new node based on the current one
2. traverse through the neighbor of the curr
3. build a new one for the neighbors not in records (dict)
4. repeat 1 - 3
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        def dfs(curr):
            for neigh in curr.neighbors:
                if neigh.val not in graph:
                    graph[neigh.val] = Node(neigh.val)
                    dfs(neigh)
                graph[curr.val].neighbors.append(graph[neigh.val])
        graph = dict()
        graph[node.val] = Node(node.val)
        dfs(node)
        return graph[node.val]
        