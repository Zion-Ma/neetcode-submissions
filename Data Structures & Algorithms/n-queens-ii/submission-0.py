class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        pos_diag = set()
        neg_diag = set()
        col = set()

        def backtrack(r: int) -> None:
            if r == n:
                self.ans += 1
                return
            for c in range(n):
                neg = r - c
                pos = r + c
                if pos in pos_diag or neg in neg_diag or c in col:
                    continue
                pos_diag.add(pos)
                neg_diag.add(neg)
                col.add(c)
                backtrack(r + 1)
                pos_diag.remove(pos)
                neg_diag.remove(neg)
                col.remove(c)
            return
            
        backtrack(0)
        return self.ans
