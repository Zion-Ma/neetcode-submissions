class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        graph = dict()
        itin = []
        for src, dst in tickets:
            if src not in graph:
                graph[src] = []
            graph[src].append(dst)
        def dfs(curr):
            while graph.get(curr, []):
                dfs(graph[curr].pop())
            itin.append(curr)
        dfs("JFK")
        return itin[::-1]
