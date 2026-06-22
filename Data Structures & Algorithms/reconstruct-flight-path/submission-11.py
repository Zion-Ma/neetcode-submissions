"""
1. sort the tickets so we can access cities by lexi-order
2. pop the top node from the stack and add its neighbors to the stack
3. if a node have no neighbors, put it to itin
4. repeat 1 - 3 until empty stack
"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        # tickets = sorted(tickets, reverse = True)
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        itin = []
        def dfs(curr):
            while graph[curr]:
                dfs(graph[curr].pop())
            itin.append(curr)
        dfs("JFK")
        return itin[::-1]
            