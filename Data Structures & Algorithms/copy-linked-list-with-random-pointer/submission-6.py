"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # original node: [new node, random node]
        new_node_dict = defaultdict(Node)
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node_dict[curr] = new_node
            curr = curr.next

        for old, new in new_node_dict.items():
            new.next = new_node_dict[old.next] if old.next else None
            new.random = new_node_dict[old.random] if old.random else None
        return new_node_dict.get(head, None)