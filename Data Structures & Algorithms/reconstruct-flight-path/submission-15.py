class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        res = []
        def dfs(src: str) -> None:
            while graph[src]:
                dfs(graph[src].pop())
            res.append(src)
        dfs("JFK")
        return res[::-1]
