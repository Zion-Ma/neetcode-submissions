class Solution:
    def numDecodings(self, s: str) -> int:
        prev1, prev2 = 1, 0
        for i in range(len(s) - 1, -1, -1):
            curr = 0
            if s[i] != '0':
                curr += prev1
                if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456")):

                    curr += prev2
            prev2 = prev1
            prev1 = curr
        return prev1

            

