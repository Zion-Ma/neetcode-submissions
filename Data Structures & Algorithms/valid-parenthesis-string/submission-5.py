class Solution:
    def checkValidString(self, s: str) -> bool:
        left, star = [], []
        for i, ch in enumerate(s):
            if ch == "(":
                left.append(i)
            elif ch == "*":
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        if len(left) > len(star):
            return False
        while left and star:
            if star[-1] < left[-1]:
                return False
            star.pop()
            left.pop()
        return len(left) == 0