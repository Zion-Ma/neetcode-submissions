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
        nodeMap: dict[Node, Node] = dict()
        curr = head
        while curr:
            nodeMap[curr] = Node(x = curr.val)
            curr = curr.next
        curr = head
        while curr:
            nodeMap[curr].next = nodeMap.get(curr.next, None)
            nodeMap[curr].random = nodeMap.get(curr.random, None)
            curr = curr.next
        return nodeMap.get(head, None)