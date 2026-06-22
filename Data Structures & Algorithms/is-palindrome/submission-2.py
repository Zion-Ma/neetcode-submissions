class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s.__len__() == 1 or s.__len__() == 0:
            return True
        l = 0
        r = s.__len__() - 1
        while l < r:
            lc = s[l]
            rc = s[r]
            if not (lc.isalpha()) and not (lc.isdigit()):
                l += 1
            elif not (rc.isalpha()) and not (rc.isdigit()):
                r -= 1
            else:
                if lc.lower() != rc.lower():
                    return False
                l += 1
                r -= 1
        return True
                
                
        
        


        
        