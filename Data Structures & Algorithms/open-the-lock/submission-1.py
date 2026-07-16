class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        queue, seen = ["0000"], {"0000"}
        deadends = set(deadends)
        hop = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr == target:
                    return hop
                for i, digit in enumerate(curr):
                    d = int(digit)
                    d_plus = str((d + 1) % 10)
                    d_minus = str(d - 1) if d != 0 else str(9)
                    plus = curr[:i] + d_plus + curr[i + 1:]
                    minus = curr[:i] + d_minus + curr[i + 1:]
                    if plus not in deadends and plus not in seen:
                        seen.add(plus)
                        queue.append(plus)
                    if minus not in deadends and minus not in seen:
                        seen.add(minus)
                        queue.append(minus)
            hop += 1
        return -1
                    
