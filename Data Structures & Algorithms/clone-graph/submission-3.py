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
        node_dict: dict[Node, Node] = dict()

        def dfs(curr_node: Node) -> None:
            if curr_node in node_dict:
                return
            new_node = Node(val = curr_node.val)
            node_dict[curr_node] = new_node
            for neighbor in curr_node.neighbors:
                dfs(neighbor)
            return

        dfs(node)
        for old_node, curr_node in node_dict.items():
            for neighbor in old_node.neighbors:
                curr_node.neighbors.append(node_dict[neighbor])
        return node_dict[node]