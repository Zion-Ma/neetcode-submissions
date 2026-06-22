class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        def valid(i, prev):
            if i in visit: return False
            visit.add(i)
            for n in graph[i]:
                if n == prev:
                    continue
                if not valid(n, i):
                    return False
            return True
        graph = defaultdict(list)
        visit = set()
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        if not valid(0, -1):
            return False
        return len(visit) == n

















        