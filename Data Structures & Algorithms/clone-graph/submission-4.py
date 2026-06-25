"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
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