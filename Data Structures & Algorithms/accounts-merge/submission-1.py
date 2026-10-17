class DSU:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        p1, p2 = self.find(i), self.find(j)
        if p1 == p2:
            return False
        s1, s2 = self.size[p1], self.size[p2]
        if s1 > s2:
            self.parent[p2] = p1
            self.size[p1] += s2
        else:
            self.parent[p1] = p2
            self.size[p2] += s1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = DSU(len(accounts))
        email_to_acc = dict()
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email in email_to_acc:
                    uf.union(i, email_to_acc[email])
                else:
                    email_to_acc[email] = i
        email_group = defaultdict(list)
        for email, i in email_to_acc.items():
            leader = uf.find(i)
            email_group[leader].append(email)
        res = []
        for leader, group in email_group.items():
            name = accounts[leader][0]
            res.append([name] + sorted(group))
        return res



