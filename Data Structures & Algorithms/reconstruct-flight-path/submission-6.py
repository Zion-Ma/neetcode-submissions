class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = {}
        for src, dst in tickets:
            if src not in graph:
                graph[src] = []
            graph[src].append(dst)
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in graph:
                return False
            temp = list(graph[src])
            for i, neigh in enumerate(temp):
                graph[src].pop(i)
                res.append(neigh)
                if dfs(neigh): return True
                graph[src].insert(i, neigh)
                res.pop()
            return False
        dfs("JFK")
        return res
                
