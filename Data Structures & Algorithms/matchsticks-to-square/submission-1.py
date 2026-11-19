class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        target_side = total // 4
        if total % 4 != 0 or max(matchsticks) > target_side:
            return False
        matchsticks.sort(reverse = True)
        def backtrack(i: int, sides: list) -> bool:
            if i == len(matchsticks):
                return True
            seen = set()
            for j in range(len(sides)):
                if matchsticks[i] + sides[j] > target_side or sides[j] in seen:
                    continue
                seen.add(sides[j])
                sides[j] += matchsticks[i]
                if backtrack(i + 1, sides):
                    return True
                sides[j] -= matchsticks[i]
            return False
        
        return backtrack(0, [0, 0, 0, 0])