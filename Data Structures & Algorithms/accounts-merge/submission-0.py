class DSU:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        p, q = self.find(i), self.find(j)
        if p == q:
            return False
        s1, s2 = self.size[p], self.size[q]
        if s1 > s2:
            self.parent[q] = p
            self.size[p] += self.size[q]
        else:
            self.parent[p] = q
            self.size[q] += self.size[p]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToacc = dict()
        uf = DSU(len(accounts))
        for i in range(len(accounts)):
            name = accounts[i][0]
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email in emailToacc:
                    uf.union(i, emailToacc[email])
                else:
                    emailToacc[email] = i
        emailGroup = defaultdict(list)
        for email, i in emailToacc.items():
            leader = uf.find(i)
            emailGroup[leader].append(email)
        res = []
        for leader, emails in emailGroup.items():
            name = accounts[leader][0]
            res.append([name] + sorted(emails))
        return res

