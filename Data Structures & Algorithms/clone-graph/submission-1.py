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
        def dfs(curr):
            for n in curr.neighbors:
                if n.val not in records:
                    records[n.val] = Node(n.val)
                    dfs(n)
                records[curr.val].neighbors.append(records[n.val])
        if node is None:
            return node
        records = dict()
        records[node.val] = Node(node.val)
        dfs(node)
        return records[node.val]
            
                
        