"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        def dfs(curr: Node) -> None:
            if curr.val in graph:
                return 
            graph[curr.val] = Node(curr.val)
            for nei in curr.neighbors:
                dfs(nei)
                graph[curr.val].neighbors.append(graph[nei.val])
        graph = dict()
        dfs(node)
        return graph[node.val]