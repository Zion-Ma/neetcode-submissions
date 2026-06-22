class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {src:[] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
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
                
