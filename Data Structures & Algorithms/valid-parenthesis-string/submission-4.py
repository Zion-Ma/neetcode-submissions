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
        while star and left:
            s = star.pop()
            l = left.pop()
            if s < l:
                return False
        return len(left) == 0 
        
            