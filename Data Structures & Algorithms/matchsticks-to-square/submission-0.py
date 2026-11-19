class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        target_side = total // 4
        if total % 4 != 0 or max(matchsticks) > target_side:
            return False

        def check_sides(sides: list) -> bool:
            for s in sides:
                if s != target_side:
                    return False
            return True

        def backtrack(i: int, sides: list) -> bool:
            if i == len(matchsticks) and check_sides(sides):
                return True
            for j in range(len(sides)):
                if matchsticks[i] + sides[j] > target_side:
                    continue
                sides[j] += matchsticks[i]
                if backtrack(i + 1, sides):
                    return True
                sides[j] -= matchsticks[i]
            return False
        
        return backtrack(0, [0, 0, 0, 0])