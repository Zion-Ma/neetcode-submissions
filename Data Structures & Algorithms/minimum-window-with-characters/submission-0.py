class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # n1, n2 = s.__len__(), t.__len__()
        # if n1 < n2:
        #     return False
        countT, windowS = {}, {}
        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)
        have, need = 0, len(countT)
        ans, leng = [-1, -1], float("inf")
        l = 0
        for i, ch in enumerate(s):
            windowS[ch] = 1 + windowS.get(ch, 0)
            if ch in countT and countT[ch] == windowS[ch]:
                have += 1
            while have == need:
                curr_leng = i - l + 1
                if curr_leng < leng:
                    ans = [l, i]
                    leng = curr_leng
                windowS[s[l]] -= 1
                if s[l] in countT and windowS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = ans
        return s[l:r+1] if leng != float("inf") else ""

            