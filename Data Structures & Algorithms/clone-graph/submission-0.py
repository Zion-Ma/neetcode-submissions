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
        queue = [node]
        node_dict = dict()
        node_dict[node.val] = Node(node.val)
        while queue:
            curr = queue.pop(0)
            for n in curr.neighbors:
                if n.val not in node_dict:
                    queue.append(n)
                    node_dict[n.val] = Node(n.val)
                node_dict[curr.val].neighbors.append(node_dict[n.val])
        return node_dict[node.val]
        