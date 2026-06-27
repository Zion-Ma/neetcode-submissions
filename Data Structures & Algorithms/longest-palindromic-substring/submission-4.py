class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        def findPali(start: int, end: int) -> tuple:
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return (start + 1, end - 1)
        max_start, max_end = 0, 0
        for i in range(len(s)):
            odd_s, odd_e = findPali(i, i)
            even_s, even_e = findPali(i, i + 1)
            if odd_e - odd_s > even_e - even_s:
                local_s, local_e = odd_s, odd_e
            else:
                local_s, local_e = even_s, even_e
            if local_e - local_s > max_end - max_start:
                 max_start, max_end = local_s, local_e 
        return s[max_start:max_end + 1]
        


                
